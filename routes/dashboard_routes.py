"""
routes/dashboard_routes.py
Handles user dashboard and complete prediction history with localization and error resilience.
"""
from datetime import datetime, timezone
import logging
from zoneinfo import ZoneInfo
from flask import Blueprint, render_template, session
from bson.objectid import ObjectId
from db import users_collection, crop_predictions_collection, disease_predictions_collection, is_db_connected
from utils.auth_utils import login_required
from utils.model_loader import get_crop_info
from utils.translations import get_crop_translation, get_disease_translation

logger = logging.getLogger("AgriAI.Dashboard")
dashboard_bp = Blueprint("dashboard", __name__)
_IST = ZoneInfo("Asia/Kolkata")


def _format_ist_timestamp(value):
    if not isinstance(value, datetime):
        return ""
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(_IST).strftime("%Y-%m-%d %H:%M")


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    user_id = session.get("user_id")
    lang = session.get("language", "en")

    user = {"username": session.get("username", "Farmer")}
    recent_crops = []
    recent_diseases = []
    total_crop_count = 0
    total_disease_count = 0

    try:
        if is_db_connected():
            if user_id:
                try:
                    db_user = users_collection.find_one({"_id": ObjectId(user_id)})
                    if db_user:
                        user = db_user
                except Exception:
                    pass

            recent_crops = list(
                crop_predictions_collection.find({"user_id": user_id})
                .sort("created_at", -1)
                .limit(5)
            )
            recent_diseases = list(
                disease_predictions_collection.find({"user_id": user_id})
                .sort("created_at", -1)
                .limit(5)
            )
            total_crop_count = crop_predictions_collection.count_documents({"user_id": user_id})
            total_disease_count = disease_predictions_collection.count_documents({"user_id": user_id})
    except Exception as e:
        logger.warning("Dashboard database query error: %s", e)

    # Localize crop names
    for c in recent_crops:
        c["created_at_ist"] = _format_ist_timestamp(c.get("created_at"))
        crop_raw = c.get("recommended_crop", "")
        c_info = get_crop_translation(crop_raw, lang)
        c["localized_crop"] = c_info.get("name", crop_raw.title())
        c["pdf_crop_details"] = get_crop_info(crop_raw, lang=lang)
        c["pdf_alternatives"] = [
            {
                "crop_key": alternative["crop_key"],
                "crop_name": get_crop_translation(alternative["crop_key"], lang).get(
                    "name", alternative["crop_key"].title()
                ),
            }
            for alternative in c.get("alternatives", [])
        ]
        if c.get("confidence") not in (None, ""):
            try:
                c["confidence"] = round(float(c["confidence"]), 2)
            except (ValueError, TypeError):
                pass

    # Localize disease names and treatment text (used by the per-row PDF report)
    for d in recent_diseases:
        d["created_at_ist"] = _format_ist_timestamp(d.get("created_at"))
        disease_raw = d.get("disease_name", "")
        d_info = get_disease_translation(disease_raw, lang)
        d["localized_disease"] = d_info.get("name", disease_raw)
        d["localized_solution"] = d_info.get("treatment", d.get("solution", ""))
        try:
            d["confidence"] = round(float(d.get("confidence", 0)), 2)
        except (ValueError, TypeError):
            d["confidence"] = 0.0

    total_predictions = total_crop_count + total_disease_count

    return render_template(
        "dashboard.html",
        user=user,
        recent_crops=recent_crops,
        recent_diseases=recent_diseases,
        total_predictions=total_predictions,
        total_crop_count=total_crop_count,
        total_disease_count=total_disease_count,
    )


@dashboard_bp.route("/history")
@login_required
def history():
    user_id = session.get("user_id")
    lang = session.get("language", "en")

    all_crops = []
    all_diseases = []

    try:
        if is_db_connected():
            all_crops = list(
                crop_predictions_collection.find({"user_id": user_id}).sort("created_at", -1)
            )
            all_diseases = list(
                disease_predictions_collection.find({"user_id": user_id}).sort("created_at", -1)
            )
    except Exception as e:
        logger.warning("History query error: %s", e)

    for c in all_crops:
        c["created_at_ist"] = _format_ist_timestamp(c.get("created_at"))
        crop_raw = c.get("recommended_crop", "")
        c_info = get_crop_translation(crop_raw, lang)
        c["localized_crop"] = c_info.get("name", crop_raw.title())
        try:
            c["confidence"] = round(float(c.get("confidence", 99.0)), 2)
        except (ValueError, TypeError):
            c["confidence"] = 99.0

    for d in all_diseases:
        d["created_at_ist"] = _format_ist_timestamp(d.get("created_at"))
        disease_raw = d.get("disease_name", "")
        d_info = get_disease_translation(disease_raw, lang)
        d["localized_disease"] = d_info.get("name", disease_raw)
        d["localized_solution"] = d_info.get("treatment", d.get("solution", ""))
        try:
            d["confidence"] = round(float(d.get("confidence", 0)), 2)
        except (ValueError, TypeError):
            d["confidence"] = 0.0

    return render_template(
        "history.html",
        all_crops=all_crops,
        all_diseases=all_diseases,
    )