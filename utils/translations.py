"""
utils/translations.py
Centralized Internationalization (i18n) for AgriAI.
Provides complete translations for English (en), Hindi (hi), and Telugu (te).
"""

LANGUAGES = {
    "en": "English",
    "hi": "हिंदी (Hindi)",
    "te": "తెలుగు (Telugu)"
}

DEFAULT_LANGUAGE = "en"

# UI String Translations
STRINGS = {
    "en": {
        "app_name": "AgriAI",
        "tagline": "AI-Powered Agriculture Platform",
        "hero_title": "Smart Farming with AI Precision",
        "hero_desc": "Empowering farmers with intelligent crop recommendations based on soil & climate data, and instant leaf disease diagnosis from photos.",
        "nav_home": "Home",
        "nav_dashboard": "Dashboard",
        "nav_crop": "Crop Recommendation",
        "nav_disease": "Disease Detection",
        "nav_history": "History",
        "nav_login": "Login",
        "nav_register": "Register",
        "nav_logout": "Logout",
        "welcome": "Welcome",
        
        # Actions
        "btn_login": "Sign In",
        "btn_register": "Create Account",
        "btn_predict_crop": "Recommend Best Crop",
        "btn_predict_disease": "Diagnose Leaf Disease",
        "btn_reset": "Reset",
        "btn_clear": "Clear Image",
        "btn_listen": "Listen (Audio)",
        "btn_stop": "Stop Audio",
        "btn_replay": "Replay",
        "btn_explore": "Get Started",
        "btn_view_history": "View Full History",
        
        # Form fields
        "nitrogen_label": "Nitrogen (N)",
        "nitrogen_desc": "Ratio in soil (0 - 140 kg/ha)",
        "phosphorus_label": "Phosphorus (P)",
        "phosphorus_desc": "Ratio in soil (5 - 145 kg/ha)",
        "potassium_label": "Potassium (K)",
        "potassium_desc": "Ratio in soil (5 - 205 kg/ha)",
        "temperature_label": "Temperature (°C)",
        "temperature_desc": "Average air temp (8 - 44 °C)",
        "humidity_label": "Relative Humidity (%)",
        "humidity_desc": "Relative humidity (14 - 100%)",
        "ph_label": "Soil pH",
        "ph_desc": "Acidity / Alkalinity (3.5 - 10.0)",
        "rainfall_label": "Rainfall (mm)",
        "rainfall_desc": "Annual precipitation (20 - 300 mm)",
        
        # Upload
        "drag_drop_title": "Drag & Drop leaf photo here",
        "drag_drop_desc": "or click to browse from device (JPG, PNG, WEBP up to 5MB)",
        "analyzing_title": "Analyzing Leaf with Deep Learning...",
        "analyzing_desc": "Running MobileNetV2 neural network for accurate disease identification",
        
        # Results
        "result_recommended_crop": "Crop to grow",
        "result_confidence": "How sure the system is",
        "result_growing_conditions": "Best conditions for growing",
        "result_season": "Best time to grow",
        "result_soil": "Best soil",
        "result_care": "How to care for the crop",
        "result_leaf_status": "Leaf health",
        "result_status_healthy": "HEALTHY LEAF",
        "result_status_diseased": "PROBLEM FOUND",
        "result_disease_detected": "Problem found",
        "result_cause": "Why this happened",
        "result_symptoms": "What you can see",
        "result_treatment": "What to do",
        "result_organic": "Natural ways to protect the crop",
        "result_prevention": "How to prevent the problem",
        "result_alternative_crops": "Other crops you can grow",
        "pdf_report_suffix": "Report",
        "pdf_model_output": "Crop name",
        "pdf_soil_climate_inputs": "Soil and weather details",
        "pdf_generated_on": "Generated on",
        
        # Dashboard
        "stat_total_predictions": "Total Predictions",
        "stat_crop_count": "Crop Recommendations",
        "stat_disease_count": "Disease Diagnoses",
        "recent_crops_title": "Recent Crop Recommendations",
        "recent_diseases_title": "Recent Disease Detections",
        "no_crops_yet": "No crop predictions yet. Run your first recommendation!",
        "no_diseases_yet": "No disease scans yet. Upload a leaf photo to diagnose!",
        "table_date": "Date & Time",
        "table_crop": "Crop",
        "table_confidence": "Confidence",
        "table_disease": "Disease",
        "table_image": "Leaf Image",
        "table_solution": "Action / Remedy",
        
        # History
        "history_title": "Prediction History",
        "history_crop_tab": "Crop Recommendations",
        "history_disease_tab": "Leaf Disease Scans",
        
        # Auth
        "auth_username": "Username",
        "auth_email": "Email Address",
        "auth_password": "Password",
        "auth_confirm_password": "Confirm Password",
        "auth_no_account": "Don't have an account?",
        "auth_have_account": "Already have an account?",
        "auth_login_prompt": "Sign in to access your agricultural dashboard",
        "auth_register_prompt": "Join AgriAI for AI-assisted smart farming",
        
        # Audio
        "audio_playing": "Playing audio...",
        "audio_stopped": "Audio stopped.",
        "audio_not_supported": "Speech synthesis is not supported on this browser.",
        
        # Messages & Errors
        "err_invalid_file": "Please upload a valid image file (PNG, JPG, JPEG, WEBP).",
        "err_too_large": "File size exceeds the 5MB limit. Please upload a smaller image.",
        "err_prediction_failed": "Prediction failed. Please ensure the image is clear and try again.",
        "err_input_missing": "Please fill out all required soil and weather parameters.",

        # Index page – feature cards & metrics
        "badge_crops_supported": "22 Crops Supported",
        "badge_disease_classes": "29 Disease Classes",
        "crop_card_desc": "Trained on verified soil and climatic parameters. Enter your Nitrogen, Phosphorus, Potassium levels, along with temperature, humidity, pH, and precipitation to receive the optimal crop choice with genuine model probability.",
        "disease_card_desc": "Leveraging a MobileNetV2 convolutional neural network. Simply snap or drag-and-drop a leaf photograph to instantly diagnose disease pathology, biological causes, symptoms, and organic & chemical treatments.",
        "badge_npk": "🧪 Soil nutrient levels",
        "badge_weather": "🌦️ Weather Integration",
        "badge_rf": "🌲 Random Forest ML",
        "badge_voice": "🔊 Multi-Language Voice",
        "badge_upload": "📸 Drag & Drop Upload",
        "badge_ai": "⚡ Instant AI Inference",
        "badge_organic": "🌿 Organic & Chemical Control",
        "badge_audio_lang": "🔊 EN / हिंदी / తెలుగు Audio",
        "metric_crop_varieties": "Crop Varieties Evaluated",
        "metric_diseases": "Plant & Leaf Diseases",
        "metric_accuracy": "Crop Model Benchmark Accuracy",
        "metric_languages": "Languages (EN / HI / TE)",

        # Crop page
        "crop_subtitle": "Provide your soil test results and local meteorological data.",
        "badge_rf_model": "Random Forest (100 Trees)",
        "quick_presets": "⚡ Quick Presets:",
        "preset_rice": "🌾 Rice",
        "preset_maize": "🌽 Maize",
        "preset_chickpea": "🧆 Chickpea",
        "preset_cotton": "👕 Cotton",
        "preset_coffee": "☕ Coffee",
        "preset_apple": "🍎 Apple",
        "section_soil_nutrients": "🧪 Soil Macronutrients (kg/ha)",
        "section_weather_soil": "🌦️ Weather & Soil Conditions",
        "badge_ai_recommendation": "✓ Crop suggestion",
        "label_model_output": "Crop name:",
        "label_opt_temperature": "🌡️ Best temperature",
        "label_opt_humidity": "💧 Best humidity",
        "label_ideal_ph": "🧪 Best soil pH",
        "label_annual_rainfall": "🌧️ Rain needed in a year",

        # Disease page
        "disease_subtitle": "Upload a clear leaf photo for deep-learning plant disease diagnosis.",
        "badge_mobilenet": "MobileNetV2 Deep Learning",
        "btn_browse": "📁 Browse Device Photo",
        "engine_select_label": "🧠 Select AI Diagnosis Model Engine",
        "engine_select_hint": "Choose between AgriAI MobileNetV2 (29 classes, fast) or Crop-Disease-Detection CNN (38 classes, extended).",
        "alt_diagnoses_label": "Other possible problems:",
        "label_model_tag": "Disease name:",
        "label_plant": "Crop:",

        # Dashboard
        "dashboard_subtitle": "Here is your agricultural AI diagnostic and recommendation summary.",

        # History page
        "history_subtitle": "Complete historical logs of your crop recommendations and leaf disease diagnoses.",
        "table_n": "N",
        "table_p": "P",
        "table_k": "K",
        "table_temp": "Temp (°C)",
        "table_humidity_col": "Humidity (%)",
        "table_ph": "pH",
        "table_rain": "Rain (mm)",
        "table_audio": "Audio",

        # Footer
        "footer_tech": "Powered by MobileNetV2 Deep Learning & Random Forest Classifier | Flask • MongoDB • Scikit-learn"
    },
    
    "hi": {
        "app_name": "एग्री-एआई (AgriAI)",
        "tagline": "एआई-संचालित कृषि मंच",
        "hero_title": "एआई की सटीकता के साथ स्मार्ट खेती",
        "hero_desc": "मिट्टी और मौसम के अनुसार सर्वोत्तम फसल सुझाव और पत्तियों की फोटो से तुरंत रोग पहचान द्वारा किसानों को सशक्त बनाना।",
        "nav_home": "होम",
        "nav_dashboard": "डैशबोर्ड",
        "nav_crop": "फसल अनुशंसा",
        "nav_disease": "रोग पहचान",
        "nav_history": "इतिहास",
        "nav_login": "लॉग इन",
        "nav_register": "रजिस्टर",
        "nav_logout": "लॉग आउट",
        "welcome": "नमस्ते",
        
        # Actions
        "btn_login": "लॉग इन करें",
        "btn_register": "नया खाता बनाएं",
        "btn_predict_crop": "सर्वोत्तम फसल जानें",
        "btn_predict_disease": "पत्ती रोग की जांच करें",
        "btn_reset": "रीसेट करें",
        "btn_clear": "फोटो हटाएं",
        "btn_listen": "ऑडियो सुनें",
        "btn_stop": "ऑडियो रोकें",
        "btn_replay": "पुनः सुनें",
        "btn_explore": "शुरू करें",
        "btn_view_history": "पूरा इतिहास देखें",
        
        # Form fields
        "nitrogen_label": "नाइट्रोजन (N)",
        "nitrogen_desc": "मिट्टी में नाइट्रोजन स्तर (0 - 140 किग्रा/हेक्टेयर)",
        "phosphorus_label": "फास्फोरस (P)",
        "phosphorus_desc": "मिट्टी में फास्फोरस स्तर (5 - 145 किग्रा/हेक्टेयर)",
        "potassium_label": "पोटेशियम (K)",
        "potassium_desc": "मिट्टी में पोटेशियम स्तर (5 - 205 किग्रा/हेक्टेयर)",
        "temperature_label": "तापमान (°C)",
        "temperature_desc": "औसत वायु तापमान (8 - 44 °C)",
        "humidity_label": "सापेक्ष आर्द्रता (%)",
        "humidity_desc": "हवा में नमी (14 - 100%)",
        "ph_label": "मिट्टी का पीएच (pH)",
        "ph_desc": "अम्लता / क्षारीयता (3.5 - 10.0)",
        "rainfall_label": "वर्षा (मिमी)",
        "rainfall_desc": "वार्षिक वर्षा (20 - 300 मिमी)",
        
        # Upload
        "drag_drop_title": "पत्ती की फोटो यहाँ खींचें और छोड़ें",
        "drag_drop_desc": "या डिवाइस से चुनने के लिए क्लिक करें (JPG, PNG, WEBP अधिकतम 5MB)",
        "analyzing_title": "डीप लर्निंग द्वारा पत्ती का विश्लेषण हो रहा है...",
        "analyzing_desc": "सटीक रोग पहचान के लिए न्यूरल नेटवर्क मॉडल चल रहा है",
        
        # Results
        "result_recommended_crop": "उगाने के लिए फसल",
        "result_confidence": "सिस्टम को कितना भरोसा है",
        "result_growing_conditions": "फसल उगाने के लिए अच्छी स्थितियां",
        "result_season": "फसल उगाने का सही समय",
        "result_soil": "अच्छी मिट्टी",
        "result_care": "फसल की देखभाल कैसे करें",
        "result_leaf_status": "पत्ती की सेहत",
        "result_status_healthy": "पत्ती स्वस्थ है",
        "result_status_diseased": "समस्या मिली",
        "result_disease_detected": "मिली हुई समस्या",
        "result_cause": "ऐसा क्यों हुआ",
        "result_symptoms": "आप क्या देख सकते हैं",
        "result_treatment": "क्या करें",
        "result_organic": "फसल बचाने के प्राकृतिक तरीके",
        "result_prevention": "समस्या से कैसे बचें",
        "result_alternative_crops": "दूसरी फसलें जिन्हें आप उगा सकते हैं",
        "pdf_report_suffix": "रिपोर्ट",
        "pdf_model_output": "फसल का नाम",
        "pdf_soil_climate_inputs": "मिट्टी और मौसम की जानकारी",
        "pdf_generated_on": "रिपोर्ट तैयार की गई",
        
        # Dashboard
        "stat_total_predictions": "कुल भविष्यवाणियां",
        "stat_crop_count": "फसल सिफारिशें",
        "stat_disease_count": "रोग निदान",
        "recent_crops_title": "हालिया फसल सिफारिशें",
        "recent_diseases_title": "हालिया रोग निदान",
        "no_crops_yet": "अभी तक कोई फसल सिफारिश नहीं है। अपनी पहली सिफारिश प्राप्त करें!",
        "no_diseases_yet": "अभी तक कोई रोग स्कैन नहीं है। जांच के लिए पत्ती की फोटो अपलोड करें!",
        "table_date": "तारीख और समय",
        "table_crop": "फसल",
        "table_confidence": "सटीकता",
        "table_disease": "रोग",
        "table_image": "पत्ती की फोटो",
        "table_solution": "उपचार / समाधान",
        
        # History
        "history_title": "पूर्वानुमान इतिहास",
        "history_crop_tab": "फसल सिफारिशें",
        "history_disease_tab": "पत्ती रोग स्कैन",
        
        # Auth
        "auth_username": "उपयोगकर्ता नाम",
        "auth_email": "ईमेल पता",
        "auth_password": "पासवर्ड",
        "auth_confirm_password": "पासवर्ड की पुष्टि करें",
        "auth_no_account": "खाता नहीं है?",
        "auth_have_account": "पहले से खाता है?",
        "auth_login_prompt": "अपने कृषि डैशबोर्ड में प्रवेश करें",
        "auth_register_prompt": "स्मार्ट खेती के लिए एग्री-एआई से जुड़ें",
        
        # Audio
        "audio_playing": "ऑडियो चल रहा है...",
        "audio_stopped": "ऑडियो रोक दिया गया।",
        "audio_not_supported": "इस ब्राउज़र में स्पीच सिंथेसिस समर्थित नहीं है।",
        
        # Messages & Errors
        "err_invalid_file": "कृपया एक मान्य छवि फ़ाइल (PNG, JPG, JPEG, WEBP) अपलोड करें।",
        "err_too_large": "फ़ाइल का आकार 5MB की सीमा से अधिक है। कृपया छोटी फ़ाइल चुनें।",
        "err_prediction_failed": "भविष्यवाणी विफल रही। कृपया साफ छवि अपलोड करें और पुनः प्रयास करें।",
        "err_input_missing": "कृपया मिट्टी और मौसम के सभी आवश्यक पैरामीटर भरें।",

        # Index page – feature cards & metrics
        "badge_crops_supported": "22 फसलें समर्थित",
        "badge_disease_classes": "29 रोग श्रेणियाँ",
        "crop_card_desc": "सत्यापित मिट्टी और जलवायु मापदंडों पर प्रशिक्षित। नाइट्रोजन, फास्फोरस, पोटाशियम, तापमान, आर्द्रता, pH और वर्षा दर्ज करें और सटीक फसल अनुशंसा प्राप्त करें।",
        "disease_card_desc": "MobileNetV2 कन्वोल्यूशनल न्यूरल नेटवर्क का उपयोग करते हुए — पत्ती की फोटो खींचें या अपलोड करें और तुरंत रोग, कारण, लक्षण, और जैविक व रासायनिक उपचार जानें।",
        "badge_npk": "🧪 मिट्टी के पोषक तत्व",
        "badge_weather": "🌦️ मौसम एकीकरण",
        "badge_rf": "🌲 रैंडम फॉरेस्ट ML",
        "badge_voice": "🔊 बहुभाषी वॉइस",
        "badge_upload": "📸 ड्रैग & ड्रॉप अपलोड",
        "badge_ai": "⚡ तत्काल AI अनुमान",
        "badge_organic": "🌿 जैविक व रासायनिक नियंत्रण",
        "badge_audio_lang": "🔊 अंग्रेज़ी / हिंदी / తెలుగు ऑडियो",
        "metric_crop_varieties": "फसल किस्में मूल्यांकित",
        "metric_diseases": "पौध व पत्ती रोग",
        "metric_accuracy": "फसल मॉडल बेंचमार्क सटीकता",
        "metric_languages": "भाषाएँ (अंग्रेज़ी / हिंदी / तेलुगु)",

        # Crop page
        "crop_subtitle": "अपनी मिट्टी जाँच रिपोर्ट और स्थानीय मौसम डेटा प्रदान करें।",
        "badge_rf_model": "रैंडम फॉरेस्ट (100 पेड़)",
        "quick_presets": "⚡ त्वरित प्रीसेट:",
        "preset_rice": "🌾 चावल",
        "preset_maize": "🌽 मक्का",
        "preset_chickpea": "🧆 चना",
        "preset_cotton": "👕 कपास",
        "preset_coffee": "☕ कॉफ़ी",
        "preset_apple": "🍎 सेब",
        "section_soil_nutrients": "🧪 मिट्टी के मुख्य पोषक तत्व (किग्रा/हेक्टेयर)",
        "section_weather_soil": "🌦️ मौसम एवं मिट्टी की स्थिति",
        "badge_ai_recommendation": "✓ फसल की सलाह",
        "label_model_output": "फसल का नाम:",
        "label_opt_temperature": "🌡️ अच्छा तापमान",
        "label_opt_humidity": "💧 हवा में अच्छी नमी",
        "label_ideal_ph": "🧪 मिट्टी का सही pH",
        "label_annual_rainfall": "🌧️ साल भर में जरूरी बारिश",

        # Disease page
        "disease_subtitle": "गहरी-शिक्षण पौध रोग निदान के लिए स्पष्ट पत्ती फोटो अपलोड करें।",
        "badge_mobilenet": "MobileNetV2 डीप लर्निंग",
        "btn_browse": "📁 डिवाइस से फोटो चुनें",
        "engine_select_label": "🧠 AI निदान मॉडल इंजन चुनें",
        "engine_select_hint": "AgriAI MobileNetV2 (29 श्रेणियाँ, तेज़) या Crop-Disease-Detection CNN (38 श्रेणियाँ, विस्तारित) में से चुनें।",
        "alt_diagnoses_label": "दूसरी संभावित समस्याएं:",
        "label_model_tag": "रोग का नाम:",
        "label_plant": "फसल:",

        # Dashboard
        "dashboard_subtitle": "यहाँ आपकी कृषि AI निदान और अनुशंसा का सारांश है।",

        # History page
        "history_subtitle": "आपकी फसल अनुशंसाओं और पत्ती रोग निदान का पूर्ण ऐतिहासिक लॉग।",
        "table_n": "नाइट्रोजन (N)",
        "table_p": "फास्फोरस (P)",
        "table_k": "पोटेशियम (K)",
        "table_temp": "तापमान (°C)",
        "table_humidity_col": "आर्द्रता (%)",
        "table_ph": "pH",
        "table_rain": "वर्षा (मिमी)",
        "table_audio": "ऑडियो",

        # Footer
        "footer_tech": "MobileNetV2 डीप लर्निंग और रैंडम फॉरेस्ट क्लासिफायर द्वारा संचालित | Flask • MongoDB • Scikit-learn"
    },
    
    "te": {
        "app_name": "అగ్రి-ఏఐ (AgriAI)",
        "tagline": "ఏఐ ఆధారిత వ్యవసాయ వేదిక",
        "hero_title": "ఏఐ ఖచ్చితత్వంతో ఆధునిక స్మార్ట్ వ్యవసాయం",
        "hero_desc": "నేల మరియు వాతావరణ పరిస్థితుల ఆధారంగా ఉత్తమ పంట సూచనలు మరియు ఆకుల ఫోటో ద్వారా తక్షణ తెగుళ్ల గుర్తింపుతో రైతులకు తోడ్పాటు.",
        "nav_home": "హోమ్",
        "nav_dashboard": "డ్యాష్‌బోర్డ్",
        "nav_crop": "పంట సిఫార్సు",
        "nav_disease": "తెగులు గుర్తింపు",
        "nav_history": "చరిత్ర",
        "nav_login": "లాగిన్",
        "nav_register": "నమోదు",
        "nav_logout": "లాగౌట్",
        "welcome": "స్వాగతం",
        
        # Actions
        "btn_login": "లాగిన్ అవ్వండి",
        "btn_register": "ఖాతా తెరవండి",
        "btn_predict_crop": "ఉత్తమ పంటను తెలుసుకోండి",
        "btn_predict_disease": "తెగులును గుర్తించండి",
        "btn_reset": "రీసెట్ చేయండి",
        "btn_clear": "ఫోటో తీసివేయండి",
        "btn_listen": "వినండి (ఆడియో)",
        "btn_stop": "ఆపండి",
        "btn_replay": "మళ్ళీ వినండి",
        "btn_explore": "ప్రారంభించండి",
        "btn_view_history": "పూర్తి చరిత్రను చూడండి",
        
        # Form fields
        "nitrogen_label": "నత్రజని (N)",
        "nitrogen_desc": "నేలలో నత్రజని పరిమాణం (0 - 140 కిలోలు/హెక్టారు)",
        "phosphorus_label": "భాస్వరం (P)",
        "phosphorus_desc": "నేలలో భాస్వరం పరిమాణం (5 - 145 కిలోలు/హెక్టారు)",
        "potassium_label": "పొటాషియం (K)",
        "potassium_desc": "నేలలో పొటాషియం పరిమాణం (5 - 205 కిలోలు/హెక్టారు)",
        "temperature_label": "ఉష్ణోగ్రత (°C)",
        "temperature_desc": "సగటు గాలి ఉష్ణోగ్రత (8 - 44 °C)",
        "humidity_label": "తేమ శాతం (%)",
        "humidity_desc": "గాలిలోని తేమ (14 - 100%)",
        "ph_label": "నేల పి.హెచ్ (pH)",
        "ph_desc": "ఆమ్లత్వం / క్షారత్వం (3.5 - 10.0)",
        "rainfall_label": "వర్షపాతం (మిమీ)",
        "rainfall_desc": "వార్షిక వర్షపాతం (20 - 300 మిమీ)",
        
        # Upload
        "drag_drop_title": "ఆకు ఫోటోను ఇక్కడ లాగి వదలండి",
        "drag_drop_desc": "లేదా ఫైల్ ఎంచుకోవడానికి క్లిక్ చేయండి (JPG, PNG, WEBP గరిష్టంగా 5MB)",
        "analyzing_title": "డీప్ లెర్నింగ్‌తో ఆకును విశ్లేషిస్తోంది...",
        "analyzing_desc": "తెగులు ఖచ్చితమైన గుర్తింపు కోసం న్యూరల్ నెట్‌వర్క్ నడుస్తోంది",
        
        # Results
        "result_recommended_crop": "పండించడానికి మంచి పంట",
        "result_confidence": "వ్యవస్థకు ఎంత నమ్మకం ఉందో",
        "result_growing_conditions": "పంట పెరగడానికి మంచి పరిస్థితులు",
        "result_season": "పంట పెంచడానికి సరైన సమయం",
        "result_soil": "మంచి నేల",
        "result_care": "పంటను ఎలా చూసుకోవాలి",
        "result_leaf_status": "ఆకు ఆరోగ్యం",
        "result_status_healthy": "ఆకు ఆరోగ్యంగా ఉంది",
        "result_status_diseased": "సమస్య కనిపించింది",
        "result_disease_detected": "కనిపించిన సమస్య",
        "result_cause": "ఇది ఎందుకు వచ్చింది",
        "result_symptoms": "మీకు కనిపించేవి",
        "result_treatment": "ఏం చేయాలి",
        "result_organic": "పంటను కాపాడే సహజ మార్గాలు",
        "result_prevention": "ఈ సమస్య రాకుండా ఎలా చూడాలి",
        "result_alternative_crops": "మీరు పండించగల ఇతర పంటలు",
        "pdf_report_suffix": "నివేదిక",
        "pdf_model_output": "పంట పేరు",
        "pdf_soil_climate_inputs": "నేల మరియు వాతావరణ వివరాలు",
        "pdf_generated_on": "రూపొందించిన సమయం",
        "badge_ai_recommendation": "✓ పంట సూచన",
        "badge_npk": "🧪 నేలలోని పోషకాలు",
        "label_model_output": "పంట పేరు:",
        "label_opt_temperature": "🌡️ పంటకు సరైన ఉష్ణోగ్రత",
        "label_opt_humidity": "💧 గాలిలో సరైన తేమ",
        "label_ideal_ph": "🧪 నేలకు సరైన pH",
        "label_annual_rainfall": "🌧️ ఏడాదికి కావాల్సిన వర్షం",
        "alt_diagnoses_label": "ఇతర సమస్యలు ఉండే అవకాశం:",
        "label_model_tag": "తెగులు పేరు:",
        "label_plant": "పంట:",
        
        # Dashboard
        "stat_total_predictions": "మొత్తం ఫలితాలు",
        "stat_crop_count": "పంట సిఫార్సులు",
        "stat_disease_count": "తెగుళ్ల నిర్ధారణలు",
        "recent_crops_title": "ఇటీవలి పంట సిఫార్సులు",
        "recent_diseases_title": "ఇటీవలి తెగులు నిర్ధారణలు",
        "no_crops_yet": "ఇంకా పంట ఫలితాలు లేవు. మీ మొదటి సిఫార్సును పొందండి!",
        "no_diseases_yet": "ఇంకా ఆకుల స్కాన్‌లు లేవు. తెగులును గుర్తించడానికి ఫోటో అప్‌లోడ్ చేయండి!",
        "table_date": "తేదీ మరియు సమయం",
        "table_crop": "పంట",
        "table_confidence": "విశ్వసనీయత",
        "table_disease": "తెగులు",
        "table_image": "ఆకు ఫోటో",
        "table_solution": "నివారణ / చర్య",
        
        # History
        "history_title": "గత రికార్డుల చరిత్ర",
        "history_crop_tab": "పంట సిఫార్సులు",
        "history_disease_tab": "తెగులు స్కాన్‌లు",
        
        # Auth
        "auth_username": "వినియోగదారు పేరు",
        "auth_email": "ఈమెయిల్ చిరునామా",
        "auth_password": "పాస్‌వర్డ్",
        "auth_confirm_password": "పాస్‌వర్డ్ నిర్ధారించండి",
        "auth_no_account": "ఖాతా లేదా?",
        "auth_have_account": "ఇప్పటికే ఖాతా ఉందా?",
        "auth_login_prompt": "మీ వ్యవసాయ డ్యాష్‌బోర్డ్‌లోకి లాగిన్ అవ్వండి",
        "auth_register_prompt": "స్మార్ట్ వ్యవసాయం కోసం అగ్రి-ఏఐలో చేరండి",
        
        # Audio
        "audio_playing": "ఆడియో వినిపిస్తోంది...",
        "audio_stopped": "ఆడియో ఆపబడింది.",
        "audio_not_supported": "ఈ బ్రౌజర్‌లో వాయిస్ సదుపాయం అందుబాటులో లేదు.",
        
        # Messages & Errors
        "err_invalid_file": "దయచేసి సరైన ఇమేజ్ ఫైల్‌ను (PNG, JPG, JPEG, WEBP) ఎంచుకోండి.",
        "err_too_large": "ఫైల్ పరిమాణం 5MB పరిమితిని మించింది. చిన్న ఫైల్‌ను ఎంచుకోండి.",
        "err_prediction_failed": "విశ్లేషణ విఫలమైంది. దయచేసి స్పష్టమైన చిత్రాన్ని అప్‌లోడ్ చేసి మళ్లీ ప్రయత్నించండి.",
        "err_input_missing": "దయచేసి అన్ని నేల మరియు వాతావరణ వివరాలను నమోదు చేయండి."
    }
}

# Crop Translations (All 22 crops)
CROPS_I18N = {
    "apple": {
        "en": {"name": "Apple", "season": "Plant in spring and harvest in autumn in mild-climate areas.", "soil": "Loamy soil that drains well (pH 6.0 - 7.0)", "care": "Cut back crowded branches once a year so air can pass through. Give balanced potassium and check for apple scab."},
        "hi": {"name": "सेब (Apple)", "season": "ठंडे इलाकों में वसंत में लगाएं और पतझड़ में फल तोड़ें।", "soil": "ऐसी दोमट मिट्टी जिसमें पानी न रुके (pH 6.0 - 7.0)", "care": "साल में एक बार घनी डालियां काटें ताकि हवा आ-जा सके। संतुलित पोटाश दें और सेब के स्कैब रोग पर नज़र रखें।"},
        "te": {"name": "ఆపిల్ (Apple)", "season": "శీతల ప్రాంతాలలో వసంతకాలంలో నాటడం, శరదృతువులో కోత.", "soil": "మంచి నీటి పారుదల గల నేలలు (pH 6.0 - 7.0)", "care": "గాలి ప్రసరణకు కత్తిరింపులు చేయాలి మరియు పోషకాలను సమతుల్యంగా అందించాలి."}
    },
    "banana": {
        "en": {"name": "Banana", "season": "Can grow all year in warm, humid areas.", "soil": "Deep, fertile soil that drains well (pH 5.5 - 7.0)", "care": "Water regularly and cover the soil around plants with dry leaves or straw. Use fertilizer rich in potassium."},
        "hi": {"name": "केला (Banana)", "season": "गर्म और नम इलाकों में साल भर उगा सकते हैं।", "soil": "गहरी, उपजाऊ और पानी निकालने वाली दोमट मिट्टी (pH 5.5 - 7.0)", "care": "नियमित पानी दें और पौधों के पास मिट्टी पर सूखे पत्ते या भूसा बिछाएं। पोटाश वाली खाद दें।"},
        "te": {"name": "అరటి (Banana)", "season": "వేడి, తేమ ఉన్న ప్రాంతాల్లో ఏడాది పొడవునా సాగు చేయవచ్చు.", "soil": "లోతైన, సారవంతమైన నేల (pH 5.5 - 7.0)", "care": "క్రమం తప్పకుండా నీరు పెట్టండి. మొక్కల చుట్టూ ఎండిన ఆకులు లేదా గడ్డి పరచండి. పొటాష్ ఎక్కువగా ఉన్న ఎరువు వేయండి."}
    },
    "blackgram": {
        "en": {"name": "Blackgram (Urad)", "season": "Grow during the rainy season or summer.", "soil": "Loamy or clay soil that drains well (pH 6.0 - 7.5)", "care": "Treat seeds with Rhizobium culture before sowing. Keep some soil moisture when flowers appear and do not let water collect around plants."},
        "hi": {"name": "उड़द (Blackgram)", "season": "बरसात या गर्मी के मौसम में उगाएं।", "soil": "दोमट या चिकनी मिट्टी जिसमें पानी न रुके (pH 6.0 - 7.5)", "care": "बुवाई से पहले बीजों में राइजोबियम मिलाएं। फूल आने पर थोड़ी नमी रखें और पौधों के पास पानी न भरने दें।"},
        "te": {"name": "మినుములు (Blackgram)", "season": "వర్షాకాలం లేదా వేసవిలో సాగు చేయండి.", "soil": "నీరు నిలవని సారవంతమైన నేల (pH 6.0 - 7.5)", "care": "విత్తే ముందు విత్తనాలకు రైజోబియం కలపండి. పూత సమయంలో నేలలో కొద్దిగా తేమ ఉంచి, మొక్కల దగ్గర నీరు నిలవకుండా చూడండి."}
    },
    "chickpea": {
        "en": {"name": "Chickpea (Gram)", "season": "Grow in the cool, dry winter season.", "soil": "Deep loamy soil that drains well (pH 6.0 - 7.5)", "care": "Use little nitrogen fertilizer. Avoid overwatering, which can harm the roots."},
        "hi": {"name": "चना (Chickpea)", "season": "ठंडे और सूखे सर्दियों के मौसम में उगाएं।", "soil": "गहरी, अच्छी जल निकासी वाली दोमट मिट्टी (pH 6.0 - 7.5)", "care": "नाइट्रोजन वाली खाद कम दें। अधिक पानी देने से जड़ों को नुकसान हो सकता है।"},
        "te": {"name": "శనగలు (Chickpea)", "season": "శీతాకాలంలో సాగు చేయండి.", "soil": "నీరు నిలవని లోతైన నేల (pH 6.0 - 7.5)", "care": "నత్రజని ఎరువు తక్కువగా వేయండి. ఎక్కువ నీరు పెడితే వేర్లు దెబ్బతింటాయి."}
    },
    "coconut": {
        "en": {"name": "Coconut", "season": "Grows all year in warm coastal areas.", "soil": "Sandy or river-plain soil (pH 5.2 - 8.0)", "care": "Give a balanced fertilizer with magnesium and boron. In summer, water around the base of each tree."},
        "hi": {"name": "नारियल (Coconut)", "season": "गर्म तटीय इलाकों में साल भर उगता है।", "soil": "रेतीली या नदी के मैदान की मिट्टी (pH 5.2 - 8.0)", "care": "मैग्नीशियम और बोरॉन वाली संतुलित खाद दें। गर्मियों में पेड़ के चारों ओर पानी दें।"},
        "te": {"name": "కొబ్బరి (Coconut)", "season": "వేడి తీర ప్రాంతాల్లో ఏడాది పొడవునా పెరుగుతుంది.", "soil": "ఇసుక లేదా నదీ మైదానపు నేల (pH 5.2 - 8.0)", "care": "మెగ్నీషియం, బోరాన్ ఉన్న సమతుల్య ఎరువు వేయండి. వేసవిలో చెట్టు చుట్టూ నీరు పెట్టండి."}
    },
    "coffee": {
        "en": {"name": "Coffee", "season": "Plant in the rainy season under shade trees.", "soil": "Loose, fertile soil with plenty of organic matter (pH 5.5 - 6.5)", "care": "Grow in partial shade. Spread fallen leaves around the soil and watch for coffee borer pests."},
        "hi": {"name": "कॉफ़ी (Coffee)", "season": "बारिश के मौसम में छायादार पेड़ों के नीचे लगाएं।", "soil": "उपजाऊ, जैविक पदार्थ वाली दोमट मिट्टी (pH 5.5 - 6.5)", "care": "हल्की छाया रखें। मिट्टी पर सूखे पत्तों की परत बिछाएं और कॉफी के तने में छेद करने वाले कीट पर नज़र रखें।"},
        "te": {"name": "కాఫీ (Coffee)", "season": "వర్షాకాలంలో నీడనిచ్చే చెట్ల కింద నాటండి.", "soil": "సేంద్రీయ పదార్థాలు ఉన్న సారవంతమైన నేల (pH 5.5 - 6.5)", "care": "కొద్దిగా నీడ ఉండేలా చూడండి. నేలపై ఎండిన ఆకుల పొర వేయండి; కాఫీ కాండంలో రంధ్రాలు చేసే పురుగులను గమనించండి."}
    },
    "cotton": {
        "en": {"name": "Cotton", "season": "Sow in the rainy season after the first rains.", "soil": "Deep black or fertile loamy soil that drains well (pH 6.0 - 7.5)", "care": "Watch for bollworms and sap-sucking pests. Prevent water from collecting, and give nitrogen fertilizer in smaller amounts at different times."},
        "hi": {"name": "कपास (Cotton)", "season": "मानसून की पहली बारिश के बाद बीज बोएं।", "soil": "गहरी काली या उपजाऊ दोमट मिट्टी (pH 6.0 - 7.5)", "care": "गुलाबी सुंडी और रस चूसने वाले कीटों से बचाएं। खेत में पानी न भरने दें और यूरिया थोड़ी-थोड़ी मात्रा में दें।"},
        "te": {"name": "పత్తి (Cotton)", "season": "తొలకరి వర్షాల తర్వాత విత్తండి.", "soil": "లోతైన నల్లరేగడి లేదా సారవంతమైన నేల (pH 6.0 - 7.5)", "care": "గులాబీ కాయతొలుచు పురుగు, రసం పీల్చే పురుగులను గమనించండి. పొలంలో నీరు నిలవకుండా చూసి, యూరియాను కొద్దికొద్దిగా వేయండి."}
    },
    "grapes": {
        "en": {"name": "Grapes", "season": "Grow in warm, fairly dry areas; prune the vines in winter.", "soil": "Deep sandy or gravelly loam that drains well (pH 6.0 - 7.5)", "care": "Support the vines on a frame and trim crowded growth. Watch for downy mildew and take action early."},
        "hi": {"name": "अंगूर (Grapes)", "season": "गर्म और कम बारिश वाले इलाकों में उगाएं; सर्दियों में बेल काट-छांट करें।", "soil": "गहरी रेतीली दोमट मिट्टी जिसमें पानी न रुके (pH 6.0 - 7.5)", "care": "बेल को सहारा देकर चढ़ाएं और घनी डालियां काटें। डाउनी फफूंदी दिखे तो जल्दी उपाय करें।"},
        "te": {"name": "ద్రాక్ష (Grapes)", "season": "వేడి, తక్కువ వర్షం ఉండే ప్రాంతాల్లో పెంచండి; చలికాలంలో తీగలను కత్తిరించండి.", "soil": "నీరు నిలవని లోతైన ఇసుక నేల (pH 6.0 - 7.5)", "care": "తీగలకు ఆధారం ఇవ్వండి, గుబురుగా ఉన్న కొమ్మలను కత్తిరించండి. డౌనీ బూజు కనిపిస్తే వెంటనే చర్య తీసుకోండి."}
    },
    "jute": {
        "en": {"name": "Jute", "season": "Grow in warm, humid weather before and during the rainy season.", "soil": "Fertile soil on river plains (pH 6.0 - 7.2)", "care": "Keep the soil moist while plants are young. Remove extra seedlings after three weeks. After harvest, soak the stems in clean water to loosen the fibers."},
        "hi": {"name": "जूट / पटसन (Jute)", "season": "बारिश से पहले और बारिश के मौसम में, जब मौसम गर्म और नम हो।", "soil": "नदी के मैदान की उपजाऊ मिट्टी (pH 6.0 - 7.2)", "care": "पौधे छोटे हों तो मिट्टी में नमी रखें। तीन सप्ताह बाद अतिरिक्त पौधे निकाल दें। कटाई के बाद तनों को साफ पानी में भिगोकर रेशे अलग करें।"},
        "te": {"name": "జనపనార (Jute)", "season": "వర్షాకాలానికి ముందు, వర్షాకాలంలో వేడి, తేమ ఉన్నప్పుడు సాగు చేయండి.", "soil": "నదీ మైదానాల్లోని సారవంతమైన నేల (pH 6.0 - 7.2)", "care": "మొక్కలు చిన్నగా ఉన్నప్పుడు నేలలో తేమ ఉంచండి. మూడు వారాల తర్వాత అదనపు మొక్కలను తీసేయండి. కోత తర్వాత కాండాలను శుభ్రమైన నీటిలో నానబెట్టి పీచును వేరు చేయండి."}
    },
    "kidneybeans": {
        "en": {"name": "Kidney Beans (Rajma)", "season": "Grow in the rainy season in hills and in winter in northern plains.", "soil": "Light, fertile soil that drains well (pH 5.5 - 6.5)", "care": "Do not let water collect around the plants. Add phosphorus fertilizer when sowing to help roots grow well."},
        "hi": {"name": "राजमा (Kidney Beans)", "season": "पहाड़ों में बारिश के मौसम में और उत्तर के मैदानी इलाकों में सर्दियों में उगाएं।", "soil": "हल्की उपजाऊ दोमट मिट्टी जिसमें पानी न रुके (pH 5.5 - 6.5)", "care": "पौधों के पास पानी न भरने दें। जड़ों की अच्छी बढ़त के लिए बुवाई के समय फास्फोरस दें।"},
        "te": {"name": "రాజ్మా (Kidney Beans)", "season": "కొండ ప్రాంతాల్లో వర్షాకాలంలో, ఉత్తర మైదానాల్లో శీతాకాలంలో సాగు చేయండి.", "soil": "నీరు నిలవని తేలికపాటి సారవంతమైన నేల (pH 5.5 - 6.5)", "care": "మొక్కల దగ్గర నీరు నిలవకుండా చూడండి. వేర్లు బాగా పెరగడానికి విత్తేటప్పుడు భాస్వరం ఎరువు వేయండి."}
    },
    "lentil": {
        "en": {"name": "Lentil (Masoor)", "season": "Grow in the winter season.", "soil": "Can grow in poor soil but does best in light loamy soil (pH 6.0 - 7.5)", "care": "Needs little water. Remove weeds during the first 45 days after the seeds sprout."},
        "hi": {"name": "मसूर (Lentil)", "season": "सर्दियों में उगाएं।", "soil": "हल्की दोमट मिट्टी सबसे अच्छी है; कम उपजाऊ मिट्टी में भी उगा सकते हैं (pH 6.0 - 7.5)", "care": "कम पानी दें। बीज उगने के बाद पहले 45 दिनों तक खेत से घास-फूस निकालते रहें।"},
        "te": {"name": "ఎర్ర కందులు (Lentil)", "season": "శీతాకాలంలో సాగు చేయండి.", "soil": "తేలికపాటి నేలలో బాగా పెరుగుతుంది (pH 6.0 - 7.5)", "care": "తక్కువ నీరు చాలు. విత్తనాలు మొలిచిన తర్వాత మొదటి 45 రోజులు కలుపు మొక్కలను తీసేయండి."}
    },
    "maize": {
        "en": {"name": "Maize (Corn)", "season": "Grow in warm weather during the rainy or winter season.", "soil": "Fertile loamy soil that drains well (pH 5.8 - 7.5)", "care": "Water the crop when tassels and ears are forming. Watch for fall armyworm and act early."},
        "hi": {"name": "मक्का (Maize / Corn)", "season": "गर्म मौसम में बरसात या सर्दियों के दौरान उगाएं।", "soil": "उपजाऊ दोमट मिट्टी जिसमें पानी न रुके (pH 5.8 - 7.5)", "care": "जब बालियां और भुट्टे बन रहे हों तब पानी दें। फॉल आर्मीवर्म दिखे तो जल्दी उपाय करें।"},
        "te": {"name": "మొక్కజొన్న (Maize)", "season": "వర్షాకాలం లేదా శీతాకాలంలో వేడి వాతావరణం ఉన్నప్పుడు సాగు చేయండి.", "soil": "సారవంతమైన, నీరు నిలవని నేల (pH 5.8 - 7.5)", "care": "కంకులు, పొత్తులు ఏర్పడే సమయంలో నీరు పెట్టండి. కత్తెర పురుగు కనిపిస్తే వెంటనే చర్య తీసుకోండి."}
    },
    "mango": {
        "en": {"name": "Mango", "season": "Grows in warm areas and flowers in winter.", "soil": "Deep, fertile river-plain or red loamy soil (pH 5.5 - 7.5)", "care": "Reduce watering before flowering. Watch for powdery mildew and mango hoppers when flowers appear."},
        "hi": {"name": "आम (Mango)", "season": "गर्म इलाकों में उगता है और सर्दियों में फूल देता है।", "soil": "गहरी उपजाऊ नदी के मैदान की या लाल दोमट मिट्टी (pH 5.5 - 7.5)", "care": "फूल आने से पहले पानी कम दें। फूल निकलते समय मधुआ कीट और सफेद फफूंद पर नज़र रखें।"},
        "te": {"name": "మామిడి (Mango)", "season": "వేడి ప్రాంతాల్లో పెరుగుతుంది, శీతాకాలంలో పూత వస్తుంది.", "soil": "లోతైన సారవంతమైన నేల (pH 5.5 - 7.5)", "care": "పూతకు ముందు నీరు తగ్గించండి. పూలు వచ్చేటప్పుడు తేనెమంచు పురుగులు, తెల్లని బూజును గమనించండి."}
    },
    "mothbeans": {
        "en": {"name": "Mothbeans (Matki)", "season": "Grow during the rainy season; it can withstand dry weather.", "soil": "Sandy or light loamy soil for dry areas (pH 6.5 - 8.0)", "care": "Needs little water and fertilizer. It helps protect the soil and make it more fertile."},
        "hi": {"name": "मोठ (Mothbeans)", "season": "बारिश के मौसम में उगाएं; यह सूखा सह सकता है।", "soil": "सूखे इलाकों की रेतीली या हल्की दोमट मिट्टी (pH 6.5 - 8.0)", "care": "कम पानी और खाद चाहिए। यह मिट्टी को बचाने और उपजाऊ बनाने में मदद करता है।"},
        "te": {"name": "బొబ్బర్లు / మోత్ బీన్స్", "season": "వర్షాకాలంలో సాగు చేయండి; ఇది ఎండను తట్టుకోగలదు.", "soil": "ఎండ ప్రాంతాలకు ఇసుక లేదా తేలికపాటి నేల (pH 6.5 - 8.0)", "care": "తక్కువ నీరు, ఎరువు చాలు. నేలను కాపాడి సారవంతం చేయడంలో సహాయపడుతుంది."}
    },
    "mungbean": {
        "en": {"name": "Mungbean (Green Gram)", "season": "Can be grown in the rainy season, winter, or summer; it grows quickly.", "soil": "Loamy or sandy loamy soil that drains well (pH 6.2 - 7.2)", "care": "Ready to harvest in 60-70 days. Control whiteflies to help prevent yellow mosaic disease."},
        "hi": {"name": "मूंग (Mungbean)", "season": "बारिश, सर्दी या गर्मी में उगा सकते हैं; फसल जल्दी तैयार होती है।", "soil": "पानी निकालने वाली दोमट या रेतीली दोमट मिट्टी (pH 6.2 - 7.2)", "care": "फसल 60-70 दिनों में तैयार होती है। पीले मोज़ेक रोग से बचाने के लिए सफेद मक्खी पर काबू रखें।"},
        "te": {"name": "పెసలు (Mungbean)", "season": "వర్షాకాలం, శీతాకాలం లేదా వేసవిలో సాగు చేయవచ్చు; త్వరగా పంట వస్తుంది.", "soil": "నీరు నిలవని సారవంతమైన నేల (pH 6.2 - 7.2)", "care": "60-70 రోజుల్లో పంట చేతికి వస్తుంది. పసుపు మచ్చల తెగులు రాకుండా తెల్లదోమను అదుపు చేయండి."}
    },
    "muskmelon": {
        "en": {"name": "Muskmelon", "season": "Summer warm season with long sunny days.", "soil": "Sandy loam rich in organic matter (pH 6.0 - 7.5)", "care": "Irrigate regularly until fruit setting, then reduce watering to concentrate sweetness."},
        "hi": {"name": "खरबूजा (Muskmelon)", "season": "गर्मी (जायद) का मौसम, धूप भरे लंबे दिन।", "soil": "जीवांश से भरपूर बलुई दोमट मिट्टी (pH 6.0 - 7.5)", "care": "फल लगने तक नियमित पानी दें, फिर मिठास बढ़ाने के लिए सिंचाई कम कर दें।"},
        "te": {"name": "కర్బూజ (Muskmelon)", "season": "వేసవి కాలం అత్యంత అనుకూలం.", "soil": "సేంద్రీయ పదార్థాలు కలిగిన ఇసుక నేలలు (pH 6.0 - 7.5)", "care": "కాయలు ఏర్పడే వరకు తేమ ఉంచాలి, తరువాత తియ్యదనం పెరగడానికి నీరు తగ్గించాలి."}
    },
    "orange": {
        "en": {"name": "Orange (Citrus)", "season": "Grows best where there are clear rainy and dry periods.", "soil": "Deep sandy loam that drains well and has no hard layer below (pH 6.0 - 7.5)", "care": "Keep water away from the trunk. Give zinc and iron nutrients when needed."},
        "hi": {"name": "संतरा (Orange / Citrus)", "season": "ऐसे इलाकों में अच्छा उगता है जहां बारिश और सूखा दोनों मौसम आते हैं।", "soil": "गहरी रेतीली दोमट मिट्टी जिसमें हवा और पानी आसानी से आ-जा सके (pH 6.0 - 7.5)", "care": "तने के पास पानी न भरने दें। जरूरत पड़ने पर जिंक और आयरन वाली खाद दें।"},
        "te": {"name": "నారింజ / బత్తాయి (Orange)", "season": "వర్షం, ఎండ వేరువేరు కాలాల్లో ఉండే ప్రాంతాల్లో బాగా పెరుగుతుంది.", "soil": "లోతైన ఇసుక నేలలో నీరు బాగా బయటకు పోవాలి (pH 6.0 - 7.5)", "care": "చెట్టు మొదల దగ్గర నీరు నిలవనివ్వకండి. అవసరమైనప్పుడు జింక్, ఐరన్ పోషకాలు ఇవ్వండి."}
    },
    "papaya": {
        "en": {"name": "Papaya", "season": "Grow in warm areas without frost; fruit can be ready in about nine months.", "soil": "Fertile loamy soil that drains well (pH 6.0 - 7.0)", "care": "Standing water can rot the stem near the soil. Plant on raised beds so extra water can drain away."},
        "hi": {"name": "पपीता (Papaya)", "season": "गर्म, पाले से मुक्त इलाकों में उगाएं; करीब 9 महीने में फल तैयार हो सकते हैं।", "soil": "उपजाऊ दोमट मिट्टी जिसमें पानी न रुके (pH 6.0 - 7.0)", "care": "तने के पास पानी रुकने से सड़न हो सकती है। पानी निकालने के लिए ऊंची क्यारी बनाकर लगाएं।"},
        "te": {"name": "బొప్పాయి (Papaya)", "season": "వేడి వాతావరణం, 9-10 నెలల్లో దిగుబడి ప్రారంభం.", "soil": "మంచి నీటి పారుదల గల సారవంతమైన నేలలు (pH 6.0 - 7.0)", "care": "నీరు నిలిస్తే మొదలు కుళ్లు తెగులు వస్తుంది; ఎత్తైన బోదెలపై నాటాలి."}
    },
    "pigeonpeas": {
        "en": {"name": "Pigeonpeas (Arhar / Toor)", "season": "Grow during the rainy season; roots grow deep into the soil.", "soil": "Deep loamy or clay loamy soil that drains well (pH 6.0 - 7.5)", "care": "Grow between rows of cereal crops if suitable. Make sure extra water drains away and add phosphorus fertilizer when sowing."},
        "hi": {"name": "अरहर / तुअर (Pigeonpeas)", "season": "बारिश के मौसम में उगाएं; इसकी जड़ें गहरी जाती हैं।", "soil": "गहरी दोमट या चिकनी मिट्टी जिसमें पानी न रुके (pH 6.0 - 7.5)", "care": "मौका हो तो अनाज की फसल की कतारों के बीच उगाएं। पानी निकलने दें और बुवाई के समय फास्फोरस दें।"},
        "te": {"name": "కందులు (Pigeonpeas / Toor)", "season": "వర్షాకాలంలో సాగు చేయండి; దీని వేర్లు లోతుగా పెరుగుతాయి.", "soil": "లోతైన సారవంతమైన, నీరు నిలవని నేల (pH 6.0 - 7.5)", "care": "అవకాశముంటే తృణధాన్యాల వరుసల మధ్య సాగు చేయండి. నీరు బయటకు పోయేలా చేసి, విత్తేటప్పుడు భాస్వరం ఎరువు వేయండి."}
    },
    "pomegranate": {
        "en": {"name": "Pomegranate", "season": "Grow in areas with little rainfall; flowering can be managed by adjusting watering.", "soil": "Light loamy to deep river-plain soil; can grow in slightly salty soil (pH 6.5 - 8.0)", "care": "Remove shoots growing from the base. Watch for bacterial blight (Telya) and fruit-boring pests."},
        "hi": {"name": "अनार (Pomegranate)", "season": "कम बारिश वाले इलाकों में उगाएं; पानी घटा-बढ़ाकर फूल आने का समय संभाल सकते हैं।", "soil": "हल्की दोमट से गहरी नदी के मैदान की मिट्टी; थोड़ी खारी मिट्टी में भी उग सकता है (pH 6.5 - 8.0)", "care": "जड़ के पास से निकलने वाली टहनियां काटें। तेल्या रोग और फल में छेद करने वाले कीटों पर नज़र रखें।"},
        "te": {"name": "దానిమ్మ (Pomegranate)", "season": "పొడి మరియు సమశీతోష్ణ ప్రాంతాలు అనుకూలం.", "soil": "తేలికపాటి గరప నేలలు (pH 6.5 - 8.0)", "care": "చెట్టు మొదళ్లలో వచ్చే పిలకలను తొలగించాలి; తెగుళ్ల నివారణకు బోర్డో మిశ్రమం పిచికారీ చేయాలి."}
    },
    "rice": {
        "en": {"name": "Rice (Paddy)", "season": "Grow in the warm rainy season where water is available.", "soil": "Clayey or river-plain soil that holds water (pH 5.5 - 7.0)", "care": "Keep 2-5 cm of water in the field while plants grow. Use balanced fertilizer and zinc sulfate as advised."},
        "hi": {"name": "धान / चावल (Paddy / Rice)", "season": "गर्म और पानी वाले इलाकों में बारिश के मौसम में उगाएं।", "soil": "चिकनी या नदी के मैदान की मिट्टी जो पानी रोक सके (pH 5.5 - 7.0)", "care": "फसल बढ़ते समय खेत में 2-5 सेमी पानी रखें। सलाह के अनुसार संतुलित खाद और जिंक सल्फेट दें।"},
        "te": {"name": "వరి (Paddy / Rice)", "season": "నీరు అందుబాటులో ఉన్న వేడి ప్రాంతాల్లో వర్షాకాలంలో సాగు చేయండి.", "soil": "నీరు నిలిచే బంకమట్టి లేదా నదీ మైదానపు నేల (pH 5.5 - 7.0)", "care": "పంట పెరిగేటప్పుడు పొలంలో 2-5 సెం.మీ నీరు ఉంచండి. సూచనల మేరకు సమతుల్య ఎరువు, జింక్ సల్ఫేట్ వేయండి."}
    },
    "watermelon": {
        "en": {"name": "Watermelon", "season": "Grow in warm, sunny summer weather.", "soil": "Fertile sandy loamy soil that drains well (pH 6.0 - 7.0)", "care": "Cover the soil with straw to keep moisture in and fruit clean. Reduce watering as harvest approaches."},
        "hi": {"name": "तरबूज (Watermelon)", "season": "गर्म और धूप वाले मौसम में, खासकर गर्मियों में उगाएं।", "soil": "उपजाऊ रेतीली दोमट मिट्टी जिसमें पानी न रुके (pH 6.0 - 7.0)", "care": "नमी बचाने और फल साफ रखने के लिए मिट्टी पर भूसा बिछाएं। कटाई पास आने पर पानी कम दें।"},
        "te": {"name": "పుచ్చకాయ (Watermelon)", "season": "వేడి, ఎండ ఎక్కువగా ఉండే వేసవిలో సాగు చేయండి.", "soil": "సారవంతమైన, నీరు నిలవని ఇసుక నేల (pH 6.0 - 7.0)", "care": "తేమ ఉండటానికి, కాయలు శుభ్రంగా ఉండటానికి నేలపై గడ్డి పరచండి. కోత దగ్గరపడే కొద్దీ నీరు తగ్గించండి."}
    }
}

# Disease Translations & Rich Pathology (All 29 Classes)
DISEASES_I18N = {
    "Apple - Apple Scab": {
        "en": {
            "name": "Apple - Apple Scab",
            "crop": "Apple",
            "status": "Diseased",
            "cause": "Apple scab is caused by the fungus Venturia inaequalis. It spreads in cool (13-24°C), wet spring weather, especially when leaves stay wet for a long time.",
            "symptoms": "Round olive-green to dark brown spots appear on the upper side of leaves. Leaves may curl, and scabby marks can form on the fruit.",
            "treatment": "Use disease-control sprays such as Captan, Mancozeb, or Difenoconazole when new buds start to open; repeat after rain as directed on the label.",
            "organic": "Spray copper hydroxide, liquid sulfur, or neem oil. Trim crowded branches so sunlight can dry the tree.",
            "prevention": "Collect and destroy fallen leaves in autumn. Plant scab-resistant varieties such as Liberty or Honeycrisp."
        },
        "hi": {
            "name": "सेब - सेब स्कैब (Apple Scab)",
            "crop": "सेब",
            "status": "रोगग्रस्त",
            "cause": "फफूंद वेंचुरिया इनेक्वलिस (Venturia inaequalis)। ठंडे (13-24°C) और नम मौसम में तेजी से फैलता है।",
            "symptoms": "पत्तियों की ऊपरी सतह पर जैतून जैसे हरे से गहरे भूरे मखमली धब्बे, पत्तियां मुड़ना और फलों पर पपड़ीदार घाव।",
            "treatment": "हरी कली अवस्था में कैप्टन (Captan), मैंकोजेब (Mancozeb) या डाइफेनोकोनाज़ोल कवकनाशी का छिड़काव करें।",
            "organic": "कॉपर हाइड्रोक्साइड, सल्फर या नीम के तेल का छिड़काव करें; धूप और हवा के लिए पेड़ की छंटाई करें।",
            "prevention": "शरद ऋतु में गिरी हुई पत्तियों को इकट्ठा करके नष्ट कर दें; रोग प्रतिरोधी किस्मों की बुवाई करें।"
        },
        "te": {
            "name": "ఆపిల్ - ఆపిల్ స్కాబ్ (Apple Scab)",
            "crop": "ఆపిల్",
            "status": "తెగులు బారిన పడింది",
            "cause": "వెంచురియా ఇనాక్వాలిస్ అనే శిలీంధ్రం వల్ల వస్తుంది. చల్లని, తడి వాతావరణంలో వేగంగా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై ముదురు ఆకుపచ్చ మరియు గోధుమ రంగు మచ్చలు ఏర్పడి ఆకులు రాలిపోతాయి, కాయలపై పొలుసులు వస్తాయి.",
            "treatment": "క్యాప్టన్ లేదా మాంకోజెబ్ శిలీంధ్ర నాశినిని వర్షాలకు ముందు పిచికారీ చేయాలి.",
            "organic": "కాపర్ హైడ్రాక్సైడ్ లేదా వేప నూనెను ఉపయోగించండి; చెట్లకు గాలి వెలుతురు తగిలేలా కత్తిరించండి.",
            "prevention": "రాలిన ఆకులను నాశనం చేయాలి; తెగులును తట్టుకునే రకాలను ఎంచుకోవాలి."
        }
    },
    "Apple - Black Rot": {
        "en": {
            "name": "Apple - Black Rot",
            "crop": "Apple",
            "status": "Diseased",
            "cause": "The fungus Botryosphaeria obtusa enters through damaged bark, dead twigs, or insect wounds, especially in warm, wet weather.",
            "symptoms": "Leaves develop round spots with purple edges and tan centers. The trunk may have damaged areas, and fruit can develop spreading brown rot rings.",
            "treatment": "Spray Captan or Thiophanate-methyl from the time new leaves appear until the flowers fall, following the product label.",
            "organic": "Cut off and burn dead or diseased wood and dried fruit. Use copper octanoate spray as directed.",
            "prevention": "Keep trees healthy with balanced fertilizer. Clean pruning tools between cuts."
        },
        "hi": {
            "name": "सेब - ब्लैक रॉट (Black Rot)",
            "crop": "सेब",
            "status": "रोगग्रस्त",
            "cause": "बोट्रियोस्फेरिया ओब्टुसा फफूंद। छाल के घावों और सूखे टहनियों के माध्यम से प्रवेश करती है।",
            "symptoms": "पत्तियों पर मेढ़क की आंख जैसे धब्बे (बैंगनी किनारे, भूरा केंद्र), तने पर घाव और फलों का काला पड़ना।",
            "treatment": "कैप्टन या थियोफैनेट-मिथाइल फफूंदनाशक का छिड़काव करें।",
            "organic": "संक्रमित टहनियों और सूखे फलों को काटकर जलाएं; कॉपर स्प्रे करें।",
            "prevention": "औजारों को विसंक्रमित रखें और पेड़ों को कीटों के घाव से बचाएं।"
        },
        "te": {
            "name": "ఆపిల్ - బ్లాక్ రాట్ (Black Rot)",
            "crop": "ఆపిల్",
            "status": "తెగులు బారిన పడింది",
            "cause": "బోట్రియోస్ఫేరియా ఒబ్టుసా శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై వలయాకార మచ్చలు, కొమ్మలపై పుండ్లు మరియు కాయలు నల్లగా కుళ్లిపోవడం.",
            "treatment": "క్యాప్టన్ లేదా థియోఫానేట్ మిథైల్ పిచికారీ చేయాలి.",
            "organic": "ఎండిన కొమ్మలను మరియు కుళ్ళిన పండ్లను కత్తిరించి కాల్చివేయాలి.",
            "prevention": "చెట్లను ఆరోగ్యంగా ఉంచాలి మరియు కత్తిరింపు పనిముట్లను శుభ్రపరచాలి."
        }
    },
    "Apple - Cedar Apple Rust": {
        "en": {
            "name": "Apple - Cedar Apple Rust",
            "crop": "Apple",
            "status": "Diseased",
            "cause": "The fungus Gymnosporangium juniperi-virginianae needs both cedar or juniper trees and apple trees to spread.",
            "symptoms": "Bright yellow-orange spots appear on top of leaves. Later, small tube-like growths may form underneath.",
            "treatment": "Spray Myclobutanil or Chlorothalonil from the time flower buds gather in clusters until the flowers fall, following the product label.",
            "organic": "In early spring, use sulfur or copper disease-control spray as directed. Remove swollen, diseased growths from nearby wild cedar or juniper trees, where practical.",
            "prevention": "Plant rust-immune cultivars (e.g., Redfree, Prima); eliminate volunteer junipers near orchards."
        },
        "hi": {
            "name": "सेब - सीडर रस्ट (Cedar Apple Rust)",
            "crop": "सेब",
            "status": "रोगग्रस्त",
            "cause": "जिम्नोस्पोरेंजियम फफूंद। इस फफूंद को अपना जीवन चक्र पूरा करने के लिए जुनिपर और सेब दोनों की जरूरत होती है।",
            "symptoms": "पत्तियों की ऊपरी सतह पर चमकीले पीले-नारंगी धब्बे और निचली सतह पर छोटे उभार।",
            "treatment": "माइक्लोबुटानिल (Myclobutanil) या क्लोरोथैलोनिल का छिड़काव करें।",
            "organic": "वसंत ऋतु में सल्फर का छिड़काव करें; बगीचे के पास से जुनिपर झाड़ियों को हटाएं।",
            "prevention": "प्रतिरोधी किस्मों का चयन करें और बगीचे के 500 मीटर के दायरे में जुनिपर न उगने दें।"
        },
        "te": {
            "name": "ఆపిల్ - సిడార్ ఆపిల్ రస్ట్ (Cedar Rust)",
            "crop": "ఆపిల్",
            "status": "తెగులు బారిన పడింది",
            "cause": "జిమ్నోస్పోరాంజియం శిలీంధ్రం వల్ల వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై ప్రకాశవంతమైన పసుపు-నారింజ రంగు మచ్చలు ఏర్పడతాయి.",
            "treatment": "మైక్లోబుటానిల్ మందును మొగ్గ దశలో పిచికారీ చేయాలి.",
            "organic": "సల్ఫర్ పిచికారీ చేయండి; తోట పరిసరాల్లో ఉండే జునిపర్ చెట్లను తొలగించండి.",
            "prevention": "తెగులు తట్టుకునే రకాలను నాటండి."
        }
    },
    "Apple - Healthy": {
        "en": {
            "name": "Apple - Healthy",
            "crop": "Apple",
            "status": "Healthy",
            "cause": "No disease was found. The leaves look healthy and green.",
            "symptoms": "The leaves are green, with no spots, drooping, or signs of fungus.",
            "treatment": "No chemical treatment required.",
            "organic": "Use compost and neem spray when needed. Water the trees regularly.",
            "prevention": "Keep the orchard clean, use balanced fertilizer, and check trees regularly."
        },
        "hi": {
            "name": "सेब - स्वस्थ (Healthy Apple)",
            "crop": "सेब",
            "status": "स्वस्थ",
            "cause": "कोई रोग या रोगाणु नहीं पाया गया। पत्तियां पूरी तरह स्वस्थ और मजबूत हैं।",
            "symptoms": "साफ, चमकदार हरी पत्तियां बिना किसी धब्बे या सिकुड़न के।",
            "treatment": "किसी भी रासायनिक उपचार की आवश्यकता नहीं है।",
            "organic": "नियमित जैविक खाद दें और कीटों से सुरक्षा हेतु नीम के तेल का छिड़काव रखें।",
            "prevention": "उचित जल निकासी, संतुलित खाद और बगीचे की नियमित सफाई बनाए रखें।"
        },
        "te": {
            "name": "ఆపిల్ - ఆరోగ్యకరమైనది (Healthy Apple)",
            "crop": "ఆపిల్",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదా వ్యాధి కారకాలు లేవు.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేకుండా పచ్చగా, కాంతివంతంగా ఉన్నాయి.",
            "treatment": "ఎటువంటి మందులు అవసరం లేదు.",
            "organic": "సమతుల్య ఎరువులు మరియు వేప కషాయం పిచికారీతో మొక్కను కాపాడుకోండి.",
            "prevention": "సరిపడా నీరు మరియు పోషకాలను క్రమం తప్పకుండా అందించండి."
        }
    },
    "Bell Pepper - Bacterial Spot": {
        "en": {
            "name": "Bell Pepper - Bacterial Spot",
            "crop": "Bell Pepper",
            "status": "Diseased",
            "cause": "The bacterium Xanthomonas campestris pv. vesicatoria spreads through splashing rain, infected seeds, and touching wet plants.",
            "symptoms": "Small, dark brown, wet-looking raised spots appear on leaves and fruit. Leaves may fall, and fruit can be damaged by strong sun.",
            "treatment": "Use a copper-based spray mixed with Mancozeb as directed on the product label.",
            "organic": "Spray copper sulfate or Bacillus subtilis bio-formulations; remove diseased plants immediately.",
            "prevention": "Use certified clean seeds treated with hot water. Water near the soil instead of over the plants, and grow a different crop in the field for three years."
        },
        "hi": {
            "name": "शिमला मिर्च - जीवाणु धब्बा (Bacterial Spot)",
            "crop": "शिमला मिर्च",
            "status": "रोगग्रस्त",
            "cause": "जैंथोमोनास बैक्टीरिया। बारिश की बूंदों और संक्रमित बीजों द्वारा फैलता है।",
            "symptoms": "पत्तियों और फलों पर गहरे भूरे रंग के पानीदार उभरे हुए धब्बे, पत्तियां गिरना।",
            "treatment": "कॉपर ऑक्सीक्लोराइड और मैंकोजेब के मिश्रण का छिड़काव करें।",
            "organic": "बेसिलस सबटिलिस (Bacillus subtilis) या कॉपर सल्फेट का छिड़काव करें; संक्रमित पौधे हटाएं।",
            "prevention": "प्रमाणित बीजों का प्रयोग करें; ड्रिप सिंचाई अपनाएं और 3 साल का फसल चक्र रखें।"
        },
        "te": {
            "name": "బెల్ పెప్పర్ - బాక్టీరియల్ స్పాట్",
            "crop": "బెల్ పెప్పర్",
            "status": "తెగులు బారిన పడింది",
            "cause": "జాంతోమోనాస్ బాక్టీరియా వల్ల వ్యాపిస్తుంది. వర్షపు తుంపర్ల ద్వారా వ్యాప్తి చెందుతుంది.",
            "symptoms": "ఆకులపై చిన్న చిన్న ముదురు గోధుమ రంగు నీటి మచ్చలు ఏర్పడతాయి.",
            "treatment": "కాపర్ ఆక్సిక్లోరైడ్ మరియు మాంకోజెబ్ కలిపి పిచికారీ చేయాలి.",
            "organic": "బాసిల్లస్ సబ్టిలిస్ జీవ నియంత్రణ మందులు వాడాలి; రాలిన ఆకులను తీసివేయాలి.",
            "prevention": "శుద్ధి చేసిన విత్తనాలు వాడాలి; పైనుంచి నీరు చల్లే పద్ధతిని నివారించాలి."
        }
    },
    "Bell Pepper - Healthy": {
        "en": {
            "name": "Bell Pepper - Healthy",
            "crop": "Bell Pepper",
            "status": "Healthy",
            "cause": "No disease was found. The plant looks strong and healthy.",
            "symptoms": "Uniform deep green leaves, firm stems, and normal blossom development.",
            "treatment": "No treatment required.",
            "organic": "Cover the soil with plant material and keep it slightly moist. Seaweed spray can also be used on the leaves.",
            "prevention": "Monitor for aphids and mites; provide calcium to prevent blossom end rot."
        },
        "hi": {
            "name": "शिमला मिर्च - स्वस्थ (Healthy Bell Pepper)",
            "crop": "शिमला मिर्च",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं। पौधा स्वस्थ और पूर्ण विकसित है।",
            "symptoms": "गहरे हरे रंग की पत्तियां, मजबूत तना और स्वस्थ फूल।",
            "treatment": "किसी दवा की आवश्यकता नहीं है।",
            "organic": "नियमित जैविक खाद और समुद्री शैवाल (सीवीड) अर्क का छिड़काव करें।",
            "prevention": "कैल्शियम की कमी न होने दें और माहू (एफिड्स) पर नजर रखें।"
        },
        "te": {
            "name": "బెల్ పెప్పర్ - ఆరోగ్యకరమైనది",
            "crop": "బెల్ పెప్పర్",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు. మొక్క పచ్చగా బలంగా ఉంది.",
            "symptoms": "ముదురు ఆకుపచ్చ రంగు ఆకులు మరియు ఆరోగ్యకరమైన పూత.",
            "treatment": "మందుల పిచికారీ అవసరం లేదు.",
            "organic": "సేంద్రీయ ఎరువులు మరియు క్రమబద్ధమైన నీటి యాజమాన్యం చేపట్టాలి.",
            "prevention": "రసం పీల్చే పురుగుల బారిన పడకుండా పసుపు జిగురు బోర్డులను వాడాలి."
        }
    },
    "Cherry - Healthy": {
        "en": {
            "name": "Cherry - Healthy",
            "crop": "Cherry",
            "status": "Healthy",
            "cause": "No disease was found. The tree looks healthy and is growing well.",
            "symptoms": "The leaves are glossy and green, with no holes, white powder, or yellowing.",
            "treatment": "No treatment required.",
            "organic": "Compost mulch, beneficial insect companion plants, and routine horticultural oils.",
            "prevention": "Ensure good air circulation through summer pruning; avoid trunk water splashing."
        },
        "hi": {
            "name": "चेरी - स्वस्थ (Healthy Cherry)",
            "crop": "चेरी",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं पाया गया। पत्तियां स्वस्थ और चमकदार हैं।",
            "symptoms": "चमकदार हरी पत्तियां बिना किसी छेद या धब्बे के।",
            "treatment": "उपचार की आवश्यकता नहीं है।",
            "organic": "कम्पोस्ट खाद दें और मित्र कीटों को बढ़ावा दें।",
            "prevention": "गर्मियों में हल्की छंटाई कर हवा का संचार बनाए रखें।"
        },
        "te": {
            "name": "చెర్రీ - ఆరోగ్యకరమైనది",
            "crop": "చెర్రీ",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "మొక్క ఆరోగ్యంగా ఉంది.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేకుండా మెరుస్తూ ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "సహజ ఎరువులను వాడండి.",
            "prevention": "సూర్యరశ్మి మరియు గాలి తగిలేలా కొమ్మలను ఉంచాలి."
        }
    },
    "Cherry - Powdery Mildew": {
        "en": {
            "name": "Cherry - Powdery Mildew",
            "crop": "Cherry",
            "status": "Diseased",
            "cause": "The fungus Podosphaera clandestina spreads more easily after warm days followed by cool, damp nights, especially in shady places.",
            "symptoms": "White powder-like patches appear on young leaves and fruit stems. Leaves may curl or wrinkle.",
            "treatment": "Use myclobutanil, trifloxystrobin, or propiconazole spray after the flower coverings fall, following the product label.",
            "organic": "Spray potassium bicarbonate (3g/L), wettable sulfur, or 10% milk-water solution in sunlight.",
            "prevention": "Trim crowded inner branches so sunlight and air can reach the tree. Do not use too much nitrogen fertilizer, as it can make new growth weak."
        },
        "hi": {
            "name": "चेरी - चूर्णिल आसिता (Powdery Mildew)",
            "crop": "चेरी",
            "status": "रोगग्रस्त",
            "cause": "पोडोस्फेरा कवक (Podosphaera)। गर्म दिन, ठंडी रातें और नमी इसके लिए अनुकूल हैं।",
            "symptoms": "पत्तियों और डंठल पर सफेद पाउडर जैसा लेप, पत्तियों का मुड़ना और सूखना।",
            "treatment": "माइक्लोबुटानिल या प्रोपिकोनाज़ोल का छिड़काव करें।",
            "organic": "पोटेशियम बाइकार्बोनेट या घुलनशील गंधक (सल्फर) का छिड़काव करें।",
            "prevention": "अत्यधिक यूरिया न दें और पेड़ के बीच से टहनियों की छंटाई करें ताकि धूप पहुंच सके।"
        },
        "te": {
            "name": "చెర్రీ - బూడిద తెగులు (Powdery Mildew)",
            "crop": "చెర్రీ",
            "status": "తెగులు బారిన పడింది",
            "cause": "పోడోస్ఫేరా శిలీంధ్రం వల్ల వస్తుంది. రాత్రి వేళల్లో తేమ ఉన్నప్పుడు వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై తెల్లటి బూడిద వంటి పొర ఏర్పడి ఆకులు ముడుచుకుపోతాయి.",
            "treatment": "మైక్లోబుటానిల్ లేదా ప్రొపికోనజోల్ పిచికారీ చేయాలి.",
            "organic": "పొటాషియం బైకార్బోనేట్ లేదా గంధకం పొడిని పిచికారీ చేయాలి.",
            "prevention": "సూర్యకాంతి సరిగ్గా తగిలేలా కొమ్మలను పలుచగా చేయాలి."
        }
    },
    "Corn (Maize) - Cercospora Leaf Spot": {
        "en": {
            "name": "Corn (Maize) - Cercospora Leaf Spot (Gray Leaf Spot)",
            "crop": "Maize",
            "status": "Diseased",
            "cause": "The fungus Cercospora zeae-maydis spreads in warm weather (25-30°C) when the air is very humid (over 90%).",
            "symptoms": "Long, rectangular tan or gray marks appear between the leaf veins and grow along the leaf.",
            "treatment": "When tassels begin to appear, use a disease-control spray containing Pyraclostrobin, Azoxystrobin, or Propiconazole, following its label.",
            "organic": "Rotate maize with crops such as pulses. A Trichoderma viride spray may also help; follow its label.",
            "prevention": "Turn infected plant remains into the soil so they break down. Choose maize varieties that can withstand this disease."
        },
        "hi": {
            "name": "मक्का - सर्कोस्पोरा पत्ती धब्बा (Gray Leaf Spot)",
            "crop": "मक्का",
            "status": "रोगग्रस्त",
            "cause": "सर्कोस्पोरा फफूंद। उच्च नमी और 25-30°C तापमान में तेजी से फैलता है।",
            "symptoms": "नसों के बीच आयताकार, भूरे-धूसर रंग के धब्बे जो पत्ती की लंबाई में समानांतर फैलते हैं।",
            "treatment": "एज़ोक्सीस्ट्रोबिन या प्रोपिकोनाज़ोल फफूंदनाशक का छिड़काव करें।",
            "organic": "ट्राइकोडर्मा विरिडी जैव कवकनाशी का प्रयोग करें; दलहनी फसलों के साथ फसल चक्र अपनाएं।",
            "prevention": "फसल के अवशेषों को जुताई कर मिट्टी में दबा दें और रोग-प्रतिरोधी संकर बीज बोएं।"
        },
        "te": {
            "name": "మొక్కజొన్న - సెర్కోస్పోరా ఆకుమచ్చ తెగులు",
            "crop": "మొక్కజొన్న",
            "status": "తెగులు బారిన పడింది",
            "cause": "సెర్కోస్పోరా జియే-మేడిస్ శిలీంధ్రం వల్ల వస్తుంది. అధిక తేమ దీనికి అనుకూలం.",
            "symptoms": "ఆకు ఈనెల మధ్య దీర్ఘచతురస్రాకార బూడిద రంగు మచ్చలు ఏర్పడతాయి.",
            "treatment": "అజాక్సిస్ట్రోబిన్ లేదా ప్రొపికోనజోల్ మందును పిచికారీ చేయాలి.",
            "organic": "ట్రైకోడెర్మా విరిడి వంటి జీవ శిలీంధ్ర నాశినులను వాడాలి.",
            "prevention": "పంట మార్పిడి పాటించాలి; తెగులును తట్టుకునే విత్తనాలను నాటాలి."
        }
    },
    "Corn (Maize) - Common Rust": {
        "en": {
            "name": "Corn (Maize) - Common Rust",
            "crop": "Maize",
            "status": "Diseased",
            "cause": "The fungus Puccinia sorghi causes this disease. Wind carries it from plant to plant in mild weather (16-25°C).",
            "symptoms": "Golden-brown to cinnamon-colored powdery pustules scattered on both upper and lower leaf surfaces.",
            "treatment": "If rust appears before tassels form, use Mancozeb, Azoxystrobin, or Tebuconazole as directed on the label.",
            "organic": "Spray neem cake extract or sulfur dust on the leaves. Bacillus subtilis may also help limit the fungus.",
            "prevention": "Plant maize varieties that can withstand rust and sow early in the season."
        },
        "hi": {
            "name": "मक्का - सामान्य रतुआ / रस्ट (Common Rust)",
            "crop": "मक्का",
            "status": "रोगग्रस्त",
            "cause": "पक्सीनिया सोरघाई फफूंद (Puccinia sorghi)। हवा द्वारा इसके बीजाणु दूर-दूर तक फैलते हैं।",
            "symptoms": "पत्ती की दोनों सतहों पर दालचीनी जैसे भूरे-सुनहरे रंग के उभरे हुए पाउडर वाले दाने।",
            "treatment": "टैबुकोनाज़ोल या मैंकोजेब कवकनाशी का छिड़काव करें।",
            "organic": "नीम की खली का अर्क या सल्फर का बुरकाव करें।",
            "prevention": "Rp जीन युक्त रतुआ-प्रतिरोधी संकर किस्में लगाएं; समय पर बुवाई करें।"
        },
        "te": {
            "name": "మొక్కజొన్న - కుంకుమ తెగులు (Common Rust)",
            "crop": "మొక్కజొన్న",
            "status": "తెగులు బారిన పడింది",
            "cause": "పక్సీనియా సోర్గి శిలీంధ్రం వల్ల గాలి ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకుల రెండు వైపులా ఇటుక రంగు లేదా గోధుమ రంగు పొక్కులు ఏర్పడతాయి.",
            "treatment": "టెబుకొనజోల్ లేదా మాంకోజెబ్ పిచికారీ చేయాలి.",
            "organic": "వేప కషాయం లేదా గంధకం పొడిని వాడాలి.",
            "prevention": "తెగులును తట్టుకునే రకాలను ఎంచుకోవాలి."
        }
    },
    "Corn (Maize) - Healthy": {
        "en": {
            "name": "Corn (Maize) - Healthy",
            "crop": "Maize",
            "status": "Healthy",
            "cause": "No disease was found. The plant is strong, with clean green leaves.",
            "symptoms": "Broad, vibrant green leaves with crisp edges and no discoloration or pustules.",
            "treatment": "No treatment required.",
            "organic": "Side-dress with vermicompost; apply seaweed extract during knee-high stage.",
            "prevention": "Maintain soil moisture at flowering; scout weekly for fall armyworm."
        },
        "hi": {
            "name": "मक्का - स्वस्थ (Healthy Corn)",
            "crop": "मक्का",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं। फसल स्वस्थ और मजबूत है।",
            "symptoms": "चौड़ी, हरी पत्तियां बिना किसी धब्बे या कीट के नुकसान के।",
            "treatment": "दवा की आवश्यकता नहीं है।",
            "organic": "वर्मीकम्पोस्ट (केंचुआ खाद) दें और जैविक वृद्धि वर्धक का प्रयोग करें।",
            "prevention": "घुटने तक की ऊंचाई पर यूरिया या खाद दें और कीटों की निगरानी रखें।"
        },
        "te": {
            "name": "మొక్కజొన్న - ఆరోగ్యకరమైనది",
            "crop": "మొక్కజొన్న",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "మొక్క ఆరోగ్యంగా ఉంది.",
            "symptoms": "ఆకులు ఎటువంటి తెగులు మచ్చలు లేకుండా పచ్చగా, బలంగా ఉన్నాయి.",
            "treatment": "ఎటువంటి మందులు అవసరం లేదు.",
            "organic": "వర్మీ కంపోస్ట్ ఎరువును అందించండి.",
            "prevention": "నీటి తడులు సమయానికి అందిస్తూ పంటను గమనించండి."
        }
    },
    "Corn (Maize) - Northern Leaf Blight": {
        "en": {
            "name": "Corn (Maize) - Northern Leaf Blight",
            "crop": "Maize",
            "status": "Diseased",
            "cause": "The fungus Exserohilum turcicum spreads in cool to mild weather (18-27°C), especially when there is heavy dew.",
            "symptoms": "Long gray-green or tan marks, about 2 to 15 cm long, start on the lower leaves.",
            "treatment": "At the first signs, spray Azoxystrobin with Difenoconazole, or Mancozeb, following the product label.",
            "organic": "Grow legumes or oilseed crops in rotation. Trichoderma harzianum can also be sprayed on leaves.",
            "prevention": "Plant resistant hybrids; plow down previous crop residue deep into the soil."
        },
        "hi": {
            "name": "मक्का - उत्तरी पत्ती झुलसा (Northern Leaf Blight)",
            "crop": "मक्का",
            "status": "रोगग्रस्त",
            "cause": "एक्सरोहिलम टर्सिकम फफूंद (Exserohilum turcicum)। मध्यम तापमान और भारी ओस में पनपता है।",
            "symptoms": "सिगार के आकार के लंबे, धूसर-भूरे रंग के धब्बे (2 से 15 सेमी लंबे), जो निचली पत्तियों से शुरू होते हैं।",
            "treatment": "एज़ोक्सीस्ट्रोबिन + डाइफेनोकोनाज़ोल का छिड़काव करें।",
            "organic": "ट्राइकोडर्मा हर्ज़िएनम का छिड़काव करें; दलहनी फसलों के साथ चक्र अपनाएं।",
            "prevention": "रोगरोधी हाइब्रिड बीज बोएं और पिछली फसल के अवशेषों को गहरी जुताई कर दबाएं।"
        },
        "te": {
            "name": "మొక్కజొన్న - నార్తర్న్ లీఫ్ బ్లైట్ (ఆకు ఎండు తెగులు)",
            "crop": "మొక్కజొన్న",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఎక్సెరోహిలమ్ టర్సికమ్ శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై చుట్ట (సిగార్) ఆకారంలో పొడవాటి బూడిద-గోధుమ రంగు మచ్చలు వస్తాయి.",
            "treatment": "అజాక్సిస్ట్రోబిన్ + డైఫెనోకోనజోల్ మందును పిచికారీ చేయాలి.",
            "organic": "ట్రైకోడెర్మా జీవ శిలీంధ్ర నాశినిని వాడాలి.",
            "prevention": "తెగులును తట్టుకునే రకాలను సాగు చేయాలి; లోతు దుక్కులు చేయాలి."
        }
    },
    "Grape - Black Rot": {
        "en": {
            "name": "Grape - Black Rot",
            "crop": "Grape",
            "status": "Diseased",
            "cause": "The fungus Guignardia bidwellii spreads when rain splashes it onto grapevines during warm, wet spring weather.",
            "symptoms": "Round reddish-brown spots and tiny black specks appear on leaves. Grapes may shrivel, turn black, and dry out.",
            "treatment": "Spray Mancozeb, Myclobutanil, or Kresoxim-methyl from the time buds open until four weeks after flowering, following the product label.",
            "organic": "Remove and destroy dried grape clusters in winter. Use copper hydroxide or lime-sulfur spray while vines are resting.",
            "prevention": "Trim crowded vines so they dry faster. Clear fallen leaves and other plant waste from the ground."
        },
        "hi": {
            "name": "अंगूर - ब्लैक रॉट (Grape Black Rot)",
            "crop": "अंगूर",
            "status": "रोगग्रस्त",
            "cause": "गुइग्नार्डिया फफूंद। गर्म और बारिश वाले वसंत मौसम में तेजी से फैलता है।",
            "symptoms": "पत्तियों पर लाल-भूरे गोल धब्बे और अंगूर के दाने सूखकर काले, झुर्रीदार मम्मी जैसे बन जाना।",
            "treatment": "मैंकोजेब, माइक्लोबुटानिल या क्रेसोक्सिम-मिथाइल का छिड़काव करें।",
            "organic": "सर्दियों में सूखे व सड़े हुए अंगूर के गुच्छों को नष्ट करें; कॉपर हाइड्रोक्साइड का छिड़काव करें।",
            "prevention": "कैनोपी की छंटाई करें ताकि धूप और हवा मिले; जमीन पर गिरे कचरे को साफ करें।"
        },
        "te": {
            "name": "ద్రాక్ష - బ్లాక్ రాట్ (Black Rot)",
            "crop": "ద్రాక్ష",
            "status": "తెగులు బారిన పడింది",
            "cause": "గుయిగ్నార్డియా శిలీంధ్రం వల్ల వర్షపు నీటి ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై ఎరుపు-గోధుమ రంగు మచ్చలు, కాయలు నల్లగా ఎండిపోయి రాలిపోతాయి.",
            "treatment": "మాంకోజెబ్ లేదా మైక్లోబుటానిల్ పిచికారీ చేయాలి.",
            "organic": "ఎండిపోయిన కాయల గుత్తులను తొలగించి కాల్చాలి; కాపర్ పిచికారీ చేయాలి.",
            "prevention": "పందిరిలో గాలి వెలుతురు ఉండేలా కొమ్మలను సరిచేయాలి."
        }
    },
    "Grape - Esca (Black Measles)": {
        "en": {
            "name": "Grape - Esca (Black Measles)",
            "crop": "Grape",
            "status": "Diseased",
            "cause": "This disease is caused by wood-rotting fungi, including Phaeoacremonium and Fomitiporia. They can enter through large cuts made when pruning.",
            "symptoms": "Leaves develop yellow and brown stripes between their veins. Grapes may get dark purple spots, and a vine can suddenly wilt and die.",
            "treatment": "There is no chemical cure. Protect fresh pruning cuts with a wound sealant containing tebuconazole.",
            "organic": "Use pruning wound paste containing Trichoderma. Do not prune in wet or rainy weather.",
            "prevention": "Clean pruning tools with 10% bleach before using them on another vine. Remove and burn dead, diseased vines."
        },
        "hi": {
            "name": "अंगूर - एस्का / ब्लैक मीजल्स (Esca)",
            "crop": "अंगूर",
            "status": "रोगग्रस्त",
            "cause": "लकड़ी सड़ाने वाले कवकों का समूह। छंटाई के बड़े घावों से बेल में प्रवेश करता है।",
            "symptoms": "पत्तियों पर 'बाघ की धारियों' जैसे पीले-भूरे निशान; अंगूर के दानों पर गहरे बैंगनी धब्बे।",
            "treatment": "इसका कोई सीधा रासायनिक इलाज नहीं है। छंटाई के तुरंत बाद घाव पर फफूंदनाशक पेस्ट लगाएं।",
            "organic": "ट्राइकोडर्मा युक्त घाव-लेप का प्रयोग करें; बारिश में कभी भी छंटाई न करें।",
            "prevention": "छंटाई के औजारों को विसंक्रमित करें; अत्यधिक संक्रमित बेलों को उखाड़कर नष्ट करें।"
        },
        "te": {
            "name": "ద్రాక్ష - ఎస్కా / బ్లాక్ మీజిల్స్ (Esca)",
            "crop": "ద్రాక్ష",
            "status": "తెగులు బారిన పడింది",
            "cause": "కొయ్యను కుళ్ళింపజేసే శిలీంధ్రాల వల్ల వస్తుంది. కత్తిరింపు గాయాల ద్వారా ప్రవేశిస్తుంది.",
            "symptoms": "ఆకులపై పులి చారల వంటి పసుపు-గోధుమ చారలు ఏర్పడతాయి, కాయలపై మచ్చలు వస్తాయి.",
            "treatment": "కత్తిరింపు గాయాలపై తక్షణమే శిలీంధ్ర నాశిని పేస్ట్ రాయాలి.",
            "organic": "ట్రైకోడెర్మా పేస్ట్ రాయాలి; వర్షంలో కత్తిరింపులు చేయకూడదు.",
            "prevention": "కత్తిరింపు పనిముట్లను శానిటైజ్ చేయాలి."
        }
    },
    "Grape - Healthy": {
        "en": {
            "name": "Grape - Healthy",
            "crop": "Grape",
            "status": "Healthy",
            "cause": "No disease was found. The vine is growing well, with clean leaves and healthy tendrils.",
            "symptoms": "The leaves are green and smooth, with no damaged edges.",
            "treatment": "No chemical treatment required.",
            "organic": "Trim the vines regularly, add compost, and use potassium silicate spray as directed.",
            "prevention": "Check vines regularly for signs of disease. Give balanced fertilizer and water the roots regularly."
        },
        "hi": {
            "name": "अंगूर - स्वस्थ (Healthy Grape)",
            "crop": "अंगूर",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं मिला। बेल स्वस्थ और मजबूत है।",
            "symptoms": "चमकदार हरी, बिना किसी दाग या धब्बे वाली स्वस्थ पत्तियां।",
            "treatment": "उपचार की आवश्यकता नहीं है।",
            "organic": "जैविक खाद दें और हल्की छंटाई से धूप बनाए रखें।",
            "prevention": "संतुलित ड्रिप सिंचाई और नियमित फसल निरीक्षण जारी रखें।"
        },
        "te": {
            "name": "ద్రాక్ష - ఆరోగ్యకరమైనది",
            "crop": "ద్రాక్ష",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేకుండా పచ్చగా, కాంతివంతంగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "సేంద్రీయ ఎరువులతో పోషకాలు అందించాలి.",
            "prevention": "డ్రిప్ ద్వారా క్రమబద్ధమైన నీటిని అందించాలి."
        }
    },
    "Grape - Leaf Blight": {
        "en": {
            "name": "Grape - Leaf Blight (Isariopsis Clavispora)",
            "crop": "Grape",
            "status": "Diseased",
            "cause": "The fungi Pseudocercospora vitis and Isariopsis spread in warm, damp weather late in the growing season.",
            "symptoms": "Large, uneven dark reddish-brown spots appear on leaves. The leaves dry, become brittle, and may fall early.",
            "treatment": "Spray Carbendazim, Mancozeb, or Pyraclostrobin upon early symptom appearance.",
            "organic": "Spray 1% Bordeaux mixture or copper oxychloride on the leaves. Remove badly affected leaves.",
            "prevention": "Trim crowded branches so air can pass through. Do not spray water over the leaves, and clear away fallen leaves."
        },
        "hi": {
            "name": "अंगूर - पत्ती झुलसा (Leaf Blight)",
            "crop": "अंगूर",
            "status": "रोगग्रस्त",
            "cause": "स्यूडोसर्कोस्पोरा / इसारिओप्सिस कवक। मौसम के अंत में गर्म और आर्द्र परिस्थितियों में फैलता है।",
            "symptoms": "पत्तियों पर अनियमित बड़े लाल-भूरे धब्बे, पत्तियां सूखकर कुरकुरी होना और समय से पहले गिरना।",
            "treatment": "कार्बेन्डाजिम या मैंकोजेब का छिड़काव करें।",
            "organic": "1% बोर्डो मिश्रण (Bordeaux mixture) या कॉपर ऑक्सीक्लोराइड का छिड़काव करें।",
            "prevention": "कैनोपी में हवा का संचार बढ़ाएं और ड्रिप सिंचाई का प्रयोग करें।"
        },
        "te": {
            "name": "ద్రాక్ష - ఆకు ఎండు తెగులు (Leaf Blight)",
            "crop": "ద్రాక్ష",
            "status": "తెగులు బారిన పడింది",
            "cause": "సూడోసెర్కోస్పోరా శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై పెద్ద ఎరుపు-గోధుమ రంగు మచ్చలు ఏర్పడి ఆకులు ఎండి రాలిపోతాయి.",
            "treatment": "కార్బెండజిమ్ లేదా మాంకోజెబ్ పిచికారీ చేయాలి.",
            "organic": "బోర్డో మిశ్రమం (1%) పిచికారీ చేయాలి.",
            "prevention": "చెట్లలో గాలి వెలుతురు ఉండేలా చూసుకోవాలి."
        }
    },
    "Peach - Bacterial Spot": {
        "en": {
            "name": "Peach - Bacterial Spot",
            "crop": "Peach",
            "status": "Diseased",
            "cause": "Bacterium Xanthomonas arboricola pv. pruni. Spread by rain, wind, and humid coastal climates.",
            "symptoms": "Angular purple-black spots on leaves that drop out producing a 'shot-hole' effect; sunken pitting on fruit.",
            "treatment": "Apply copper sprays during dormancy and low rates of oxytetracycline during the growing season.",
            "organic": "Dormant copper octanoate sprays; prune to promote fast foliage drying.",
            "prevention": "Plant resistant peach varieties (e.g., Candor, Biscoe); avoid planting in extremely sandy, nutrient-leached soils."
        },
        "hi": {
            "name": "आड़ू - जीवाणु धब्बा (Bacterial Spot)",
            "crop": "आड़ू",
            "status": "रोगग्रस्त",
            "cause": "जैंथोमोनास बैक्टीरिया। बारिश और हवा के माध्यम से तेजी से फैलता है।",
            "symptoms": "पत्तियों पर कोणीय बैंगनी-काले धब्बे जो सूखकर गिर जाते हैं और छर्रे जैसे छेद (shot-hole) बन जाते हैं।",
            "treatment": "सुप्तावस्था में कॉपर और विकास के समय ऑक्सीटेट्रासाइक्लिन का छिड़काव करें।",
            "organic": "सर्दियों में कॉपर ऑक्टानोएट स्प्रे करें; धूप हेतु पेड़ की छंटाई करें।",
            "prevention": "रोग प्रतिरोधी किस्में लगाएं और संतुलित पोषण बनाए रखें।"
        },
        "te": {
            "name": "పీచ్ - బాక్టీరియల్ స్పాట్",
            "crop": "పీచ్",
            "status": "తెగులు బారిన పడింది",
            "cause": "జాంతోమోనాస్ బాక్టీరియా వల్ల వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై కోణీయ మచ్చలు ఏర్పడి ఆకులు తూట్లు పడతాయి.",
            "treatment": "కాపర్ మందులు లేదా ఆక్సిటెట్రాసైక్లిన్ పిచికారీ చేయాలి.",
            "organic": "శీతాకాలంలో కాపర్ పిచికారీ చేయాలి.",
            "prevention": "తెగులు తట్టుకునే రకాలను నాటాలి."
        }
    },
    "Peach - Healthy": {
        "en": {
            "name": "Peach - Healthy",
            "crop": "Peach",
            "status": "Healthy",
            "cause": "No disease was found. The plant has healthy new shoots and clean leaves.",
            "symptoms": "The leaves are long and shiny, with toothed edges and a bright green color.",
            "treatment": "No treatment required.",
            "organic": "Use compost tea, paint the trunk white to protect it from strong sun, and cover the soil with natural material.",
            "prevention": "Scout for peach tree borers and oriental fruit moth; maintain uniform watering."
        },
        "hi": {
            "name": "आड़ू - स्वस्थ (Healthy Peach)",
            "crop": "आड़ू",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं पाया गया। पेड़ पूरी तरह स्वस्थ है।",
            "symptoms": "लंबी, चमकदार हरी पत्तियां बिना किसी छेद या धब्बे के।",
            "treatment": "दवा की आवश्यकता नहीं है।",
            "organic": "कम्पोस्ट खाद दें और तने पर सफेदी लगाएं ताकि धूप से नुकसान न हो।",
            "prevention": "तना छेदक कीट पर नजर रखें और उचित सिंचाई बनाए रखें।"
        },
        "te": {
            "name": "పీచ్ - ఆరోగ్యకరమైనది",
            "crop": "పీచ్",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు పొడవుగా, పచ్చగా ఆరోగ్యంగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "సేంద్రీయ ఎరువులను వాడండి.",
            "prevention": "బోదె పురుగులు ఆశించకుండా జాగ్రత్త పడాలి."
        }
    },
    "Potato - Early Blight": {
        "en": {
            "name": "Potato - Early Blight",
            "crop": "Potato",
            "status": "Diseased",
            "cause": "The fungus Alternaria solani spreads in warm weather (24-29°C), especially when wet and dry periods alternate.",
            "symptoms": "Older leaves develop round dark-brown spots with rings like a target and a yellow edge.",
            "treatment": "When the disease is spreading, use Chlorothalonil, Mancozeb, or Azoxystrobin spray every 7-10 days, following the product label.",
            "organic": "Spray copper hydroxide or Bacillus amyloliquefaciens as directed. Remove affected lower leaves.",
            "prevention": "For three years, grow crops other than potato, tomato, pepper, or eggplant in this field. Keep plants healthy with balanced fertilizer."
        },
        "hi": {
            "name": "आलू - अगेती झुलसा (Potato Early Blight)",
            "crop": "आलू",
            "status": "रोगग्रस्त",
            "cause": "अल्टरनेरिया सोलानी फफूंद। गर्म तापमान (24-29°C) और सूखे-गीले मौसम में फैलता है।",
            "symptoms": "पुरानी पत्तियों पर गोल भूरे धब्बे जिनमें 'लक्ष्य-पट्ट' (target board) जैसी संकेंद्री वलय होती हैं और पीला घेरा होता है।",
            "treatment": "क्लोरोथैलोनिल, मैंकोजेब या एज़ोक्सीस्ट्रोबिन का छिड़काव 7-10 दिनों के अंतराल पर करें।",
            "organic": "कॉपर हाइड्रोक्साइड या बेसिलस का छिड़काव करें; निचली संक्रमित पत्तियों को तोड़ें।",
            "prevention": "3 साल का फसल चक्र अपनाएं; अत्यधिक या असंतुलित यूरिया से बचें।"
        },
        "te": {
            "name": "బంగాళాదుంప - ప్రారంభ తెగులు (Early Blight)",
            "crop": "బంగాళాదుంప",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఆల్టర్నేరియా సోలాని శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై వలయాకారపు గోధుమ రంగు మచ్చలు (టార్గెట్ బోర్డ్ ఆకారం) ఏర్పడతాయి.",
            "treatment": "క్లోరోథలోనిల్ లేదా మాంకోజెబ్ మందును పిచికారీ చేయాలి.",
            "organic": "కాపర్ లేదా జీవ శిలీంధ్ర నాశిని వాడాలి; కింది ఆకులను తొలగించాలి.",
            "prevention": "పంట మార్పిడి పాటించాలి; మొక్కలను ఆరోగ్యంగా ఉంచాలి."
        }
    },
    "Potato - Healthy": {
        "en": {
            "name": "Potato - Healthy",
            "crop": "Potato",
            "status": "Healthy",
            "cause": "No disease was found. The plant looks strong and its leaves are a healthy dark green.",
            "symptoms": "The leaves are evenly dark green, the stems stand upright, and the plant is clean.",
            "treatment": "No treatment required.",
            "organic": "Pile soil around the stems and add compost or neem cake.",
            "prevention": "Keep soil around the stems to cover the potatoes and protect them from sunlight. Check for Colorado potato beetles."
        },
        "hi": {
            "name": "आलू - स्वस्थ (Healthy Potato)",
            "crop": "आलू",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं मिला। पौधे स्वस्थ हैं और कंद निर्माण अच्छा हो रहा है।",
            "symptoms": "गहरे हरे रंग की संयुक्त पत्तियां, मजबूत तना और स्वस्थ पौधे।",
            "treatment": "दवा की आवश्यकता नहीं है।",
            "organic": "पौधों पर मिट्टी चढ़ाएं और नीम की खली व कम्पोस्ट खाद दें।",
            "prevention": "कंदों को धूप से बचाने के लिए अच्छी मिट्टी चढ़ाएं और कीटों पर नज़र रखें।"
        },
        "te": {
            "name": "బంగాళాదుంప - ఆరోగ్యకరమైనది",
            "crop": "బంగాళాదుంప",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు ముదురు ఆకుపచ్చగా ఆరోగ్యంగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "మొక్క మొదళ్లలో మట్టిని ఎగదోయాలి మరియు సేంద్రీయ ఎరువులు వేయాలి.",
            "prevention": "దుంపలకు ఎండ తగలకుండా మట్టిని కప్పి ఉంచాలి."
        }
    },
    "Potato - Late Blight": {
        "en": {
            "name": "Potato - Late Blight",
            "crop": "Potato",
            "status": "Diseased",
            "cause": "Phytophthora infestans, a fungus-like organism, causes this disease. It spreads quickly in cool (10-21°C), damp, foggy weather when leaves stay wet.",
            "symptoms": "Dark, wet-looking marks spread from leaf tips and edges. In humid mornings, a white fuzzy growth may appear underneath the leaves.",
            "treatment": "At the first signs, use a disease-control spray containing Metalaxyl-Mancozeb, Cymoxanil, or Dimethomorph, following the product label.",
            "organic": "Preventive copper sulfate sprays (Bordeaux mixture); destroy infected cull piles; harvest only during dry weather.",
            "prevention": "Plant certified seed potatoes that can withstand late blight. Water near the soil, not over the leaves, and remove potato plants that grow from leftover tubers."
        },
        "hi": {
            "name": "आलू - पछेती झुलसा (Potato Late Blight)",
            "crop": "आलू",
            "status": "रोगग्रस्त",
            "cause": "फाइटोफ्थोरा इन्फेस्टन्स (Phytophthora infestans)। ठंडा (10-21°C), कोहरे और नमी वाला मौसम इसके लिए अत्यंत अनुकूल है।",
            "symptoms": "पत्तियों के किनारों पर तेजी से फैलते हुए पानीदार काले-भूरे धब्बे, सुबह के समय निचली सतह पर सफेद मखमली फफूंद।",
            "treatment": "मेटालेक्सिल + मैंकोजेब (Metalaxyl-Mancozeb) या साइमोक्सानिल का तुरंत छिड़काव करें।",
            "organic": "बोर्डो मिश्रण का निवारक छिड़काव करें; संक्रमित पौधों को उखाड़कर नष्ट करें।",
            "prevention": "प्रमाणित रोगरोधी बीज आलू लगाएं; ड्रिप सिंचाई अपनाएं और खेतों में पानी न रुकने दें।"
        },
        "te": {
            "name": "బంగాళాదుంప - లేట్ బ్లైట్ (చివరి దశ తెగులు)",
            "crop": "బంగాళాదుంప",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఫైటోఫ్తోరా ఇన్ఫెస్టాన్స్ అనే శిలీంధ్రం వల్ల వస్తుంది. చల్లని, తేమతో కూడిన వాతావరణంలో పంటను పూర్తిగా నాశనం చేస్తుంది.",
            "symptoms": "ఆకుల అంచులపై నల్లటి నీటి మచ్చలు ఏర్పడి, ఉదయం వేళల్లో ఆకు వెనుక తెల్లటి బూజు కనిపిస్తుంది.",
            "treatment": "మెటలాక్సిల్ + మాంకోజెబ్ లేదా డైమెథోమార్ఫ్ తక్షణమే పిచికారీ చేయాలి.",
            "organic": "బోర్డో మిశ్రమం పిచికారీ చేయాలి; తెగులు సోకిన మొక్కలను నాశనం చేయాలి.",
            "prevention": "ధృవీకరించిన విత్తన దుంపలను మాత్రమే వాడాలి; పైనుంచి నీరు చల్లకూడదు."
        }
    },
    "Strawberry - Healthy": {
        "en": {
            "name": "Strawberry - Healthy",
            "crop": "Strawberry",
            "status": "Healthy",
            "cause": "No disease was found. The plant is growing well and its leaves look healthy.",
            "symptoms": "The leaves are glossy green and grow in groups of three, with toothed edges and no spots.",
            "treatment": "No treatment required.",
            "organic": "Cover the soil with pine needles or straw, and use compost tea or natural fertilizers.",
            "prevention": "After harvest, clear and renew the growing bed. Water near the plants and keep the plastic soil cover in place."
        },
        "hi": {
            "name": "स्ट्रॉबेरी - स्वस्थ (Healthy Strawberry)",
            "crop": "स्ट्रॉबेरी",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं मिला। पौधे स्वस्थ और फलने-फूलने के लिए तैयार हैं।",
            "symptoms": "चमकदार हरी तीन-पत्ती वाली पत्तियां बिना किसी दाग या झुलसन के।",
            "treatment": "दवा की आवश्यकता नहीं है।",
            "organic": "पुआल या चीड़ की पत्तियों की मल्चिंग करें और जैविक खाद दें।",
            "prevention": "ड्रिप सिंचाई का प्रयोग करें ताकि पत्तियां गीली न रहें।"
        },
        "te": {
            "name": "స్ట్రాబెర్రీ - ఆరోగ్యకరమైనది",
            "crop": "స్ట్రాబెర్రీ",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేకుండా పచ్చగా, కాంతివంతంగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "నేలపై గడ్డి పరచండి.",
            "prevention": "డ్రిప్ పద్ధతిలో నీరు అందిస్తూ ఆకులు తడవకుండా చూడాలి."
        }
    },
    "Strawberry - Leaf Scorch": {
        "en": {
            "name": "Strawberry - Leaf Scorch",
            "crop": "Strawberry",
            "status": "Diseased",
            "cause": "The fungus Diplocarpon earlianum spreads in rain splashes and when leaves stay wet for a long time.",
            "symptoms": "Many small purple or dark-brown spots join together. The leaf may turn brown, curl up, and dry out.",
            "treatment": "Use a disease-control spray containing Captan, Thiophanate-methyl, or Pyraclostrobin, following the product label.",
            "organic": "Mow and bury old leaves after harvest; spray copper soap or potassium bicarbonate.",
            "prevention": "Space plants generously on raised beds; remove old infected foliage; use drip tape under mulch."
        },
        "hi": {
            "name": "स्ट्रॉबेरी - पत्ती झुलसा (Leaf Scorch)",
            "crop": "स्ट्रॉबेरी",
            "status": "रोगग्रस्त",
            "cause": "डिप्लोकार्पोन अर्लियानम फफूंद (Diplocarpon earlianum)। बारिश की बूंदों और नमी से फैलता है।",
            "symptoms": "पत्तियों पर छोटे बैंगनी-भूरे धब्बे जो आपस में मिलकर पूरी पत्ती को भूरा और झुलसा हुआ बना देते हैं।",
            "treatment": "कैप्टन या थियोफैनेट-मिथाइल फफूंदनाशक का छिड़काव करें।",
            "organic": "कटाई के बाद पुरानी पत्तियों को हटा दें; कॉपर सोप या पोटेशियम बाइकार्बोनेट का छिड़काव करें।",
            "prevention": "उठी हुई क्यारियों पर उचित दूरी पर पौधे लगाएं और प्लास्टिक मल्च का उपयोग करें।"
        },
        "te": {
            "name": "స్ట్రాబెర్రీ - ఆకు మాకుడు తెగులు (Leaf Scorch)",
            "crop": "స్ట్రాబెర్రీ",
            "status": "తెగులు బారిన పడింది",
            "cause": "డిప్లోకార్పన్ ఎర్లియానం శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై చిన్న ఊదా రంగు మచ్చలు ఏర్పడి క్రమంగా ఆకు మొత్తం ఎండిపోతుంది.",
            "treatment": "క్యాప్టన్ లేదా థియోఫానేట్ మిథైల్ పిచికారీ చేయాలి.",
            "organic": "పాత ఆకులను కత్తిరించి నాశనం చేయాలి; కాపర్ పిచికారీ చేయాలి.",
            "prevention": "మొక్కల మధ్య సరైన దూరం పాటించాలి; డ్రిప్ ఇరిగేషన్ వాడాలి."
        }
    },
    "Tomato - Bacterial Spot": {
        "en": {
            "name": "Tomato - Bacterial Spot",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Bacterium Xanthomonas vesicatoria. Survives in crop debris and seed; spreads via rain splash and touching wet foliage.",
            "symptoms": "Small, dark, greasy water-soaked spots with yellow halos on leaves; raised, scabby circular spots on green fruit.",
            "treatment": "Use a copper-based spray mixed with Mancozeb as directed on the product label.",
            "organic": "Spray Bacillus subtilis or copper hydroxide on the leaves. Trim low shoots to let air pass through.",
            "prevention": "Use certified hot water-treated seed; stake plants; practice 3-year crop rotation avoiding all nightshades."
        },
        "hi": {
            "name": "टमाटर - जीवाणु धब्बा (Tomato Bacterial Spot)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "जैंथोमोनास बैक्टीरिया (Xanthomonas)। संक्रमित बीज और बारिश की फुहारों से फैलता है।",
            "symptoms": "पत्तियों पर छोटे काले-भूरे पानीदार धब्बे जिनके चारों ओर पीला घेरा होता है; कच्चे फलों पर उभरे हुए खुरदुरे धब्बे।",
            "treatment": "कॉपर ऑक्सीक्लोराइड को मैंकोजेब के साथ मिलाकर छिड़काव करें।",
            "organic": "बेसिलस सबटिलिस जैव कीटनाशक का छिड़काव करें; नीचे की संक्रमित शाखाएं काटें।",
            "prevention": "प्रमाणित बीजों का ही प्रयोग करें; पौधों को बांस से सहारा दें; 3 साल का फसल चक्र रखें।"
        },
        "te": {
            "name": "టమోటా - బాక్టీరియల్ స్పాట్",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "జాంతోమోనాస్ బాక్టీరియా వల్ల వర్షపు తుంపర్ల ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై చిన్న చిన్న నల్లటి మచ్చలు ఏర్పడతాయి; కాయలపై గరుకు మచ్చలు వస్తాయి.",
            "treatment": "కాపర్ ఆక్సిక్లోరైడ్ మరియు మాంకోజెబ్ కలిపి పిచికారీ చేయాలి.",
            "organic": "జీవ బాక్టీరియా నాశినులను వాడాలి; రాలిన ఆకులను తీసివేయాలి.",
            "prevention": "మొక్కలను కర్రలతో కట్టాలి; రాత్రి వేళల్లో తడి ఉండకుండా చూడాలి."
        }
    },
    "Tomato - Early Blight": {
        "en": {
            "name": "Tomato - Early Blight",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "The fungus Alternaria solani can remain in soil and old crop waste. It spreads in warm, wet weather.",
            "symptoms": "Older lower leaves develop round, ringed spots with a yellow edge and may fall early.",
            "treatment": "Apply Chlorothalonil, Mancozeb, or Azoxystrobin every 7 to 14 days.",
            "organic": "Cover the soil with straw or black plastic to stop soil splashing onto plants. Use copper spray or neem oil as directed.",
            "prevention": "Prune bottom 12 inches of foliage; stake tomatoes for airflow; rotate crops annually."
        },
        "hi": {
            "name": "टमाटर - अगेती झुलसा (Tomato Early Blight)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "अल्टरनेरिया सोलानी कवक (Alternaria solani)। मिट्टी और पुरानी पत्तियों में जीवित रहता है।",
            "symptoms": "निचली पत्तियों पर छल्लेदार (target) गोल भूरे धब्बे, पत्तियों का पीला पड़ना और गिरना।",
            "treatment": "क्लोरोथैलोनिल या मैंकोजेब का 7-10 दिनों के अंतराल पर छिड़काव करें।",
            "organic": "जमीन पर पुआल की मल्चिंग करें ताकि मिट्टी पत्तियों पर न उछले; नीम का तेल छिड़कें।",
            "prevention": "पौधे के नीचे की 1 फीट पत्तियों को काट दें; पौधों को सहारा दें और हर साल फसल बदलें।"
        },
        "te": {
            "name": "టమోటా - ప్రారంభ తెగులు (Early Blight)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఆల్టర్నేరియా సోలాని శిలీంధ్రం వల్ల వస్తుంది. నేలలోని తేమ ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "కింది ఆకులపై వలయాకార మచ్చలు ఏర్పడి ఆకులు పసుపు రంగులోకి మారి రాలిపోతాయి.",
            "treatment": "క్లోరోథలోనిల్ లేదా మాంకోజెబ్ మందును పిచికారీ చేయాలి.",
            "organic": "నేలపై ప్లాస్టిక్ కవర్ లేదా గడ్డి పరచండి; వేపనూనె పిచికారీ చేయండి.",
            "prevention": "కింది భాగంలోని ఆకులను కత్తిరించాలి; కర్రల సహాయంతో మొక్కలను నిలబెట్టాలి."
        }
    },
    "Tomato - Healthy": {
        "en": {
            "name": "Tomato - Healthy",
            "crop": "Tomato",
            "status": "Healthy",
            "cause": "No disease was found. The plant is strong, with green leaves and sturdy stems.",
            "symptoms": "The leaves are clean and green, with no spots, curling, patchy patterns, or signs of blight.",
            "treatment": "No chemical treatment required.",
            "organic": "Maintain regular watering, organic compost, calcium-rich soil amendments to prevent blossom end rot.",
            "prevention": "Scout for whiteflies, hornworms, and spider mites; stake and prune regularly."
        },
        "hi": {
            "name": "टमाटर - स्वस्थ (Healthy Tomato)",
            "crop": "टमाटर",
            "status": "स्वस्थ",
            "cause": "कोई रोग या कवक नहीं है। पौधा पूरी तरह स्वस्थ और मजबूत है।",
            "symptoms": "स्वच्छ, सुगंधित हरी पत्तियां बिना किसी धब्बे, मोज़ेक या सड़न के।",
            "treatment": "किसी दवा की जरूरत नहीं है।",
            "organic": "नियमित जैविक खाद दें और फल गलन से बचाव हेतु कैल्शियम युक्त चूना या राख दें।",
            "prevention": "सफेद मक्खी और इल्लियों की निगरानी रखें; पौधों को सहारा दें।"
        },
        "te": {
            "name": "టమోటా - ఆరోగ్యకరమైనది",
            "crop": "టమోటా",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేదా ముడతలు లేకుండా పచ్చగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "సమతుల్య సేంద్రీయ ఎరువులు మరియు కాల్షియం అందించాలి.",
            "prevention": "తెల్లదోమ మరియు ఇతర పురుగులను గమనిస్తూ ఉండాలి."
        }
    },
    "Tomato - Late Blight": {
        "en": {
            "name": "Tomato - Late Blight",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Phytophthora infestans, a fungus-like organism, causes this disease. It spreads quickly in cool, wet, cloudy weather.",
            "symptoms": "Dark, wet-looking marks spread quickly on leaves and stems. White fuzzy growth may appear underneath leaves, and fruit may develop soft brown rot.",
            "treatment": "Apply Cymoxanil, Dimethomorph, or Metalaxyl-Mancozeb immediately at first sign.",
            "organic": "Use copper sulfate (Bordeaux mixture) as directed. Remove badly affected plants, place them in a bag, and dispose of them away from the field.",
            "prevention": "Plant late-blight-resistant varieties (e.g., Defiant, Mountain Merit); do not overhead irrigate."
        },
        "hi": {
            "name": "टमाटर - पछेती झुलसा (Tomato Late Blight)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "फाइटोफ्थोरा इन्फेस्टन्स फफूंद। ठंडे, बादल छाए और बारिश वाले मौसम में यह कुछ ही दिनों में पूरी फसल नष्ट कर सकता है।",
            "symptoms": "पत्तियों और तने पर तेजी से फैलते हुए पानीदार काले धब्बे, पत्ती के नीचे सफेद फफूंद और फलों का सड़ना।",
            "treatment": "साइमोक्सानिल या मेटालेक्सिल-मैंकोजेब का तुरंत छिड़काव करें।",
            "organic": "बोर्डो मिश्रण का छिड़काव करें; गंभीर रूप से बीमार पौधों को तुरंत उखाड़कर नष्ट करें।",
            "prevention": "रोगरोधी किस्में लगाएं और शाम के समय पौधों पर पानी का छिड़काव न करें।"
        },
        "te": {
            "name": "టమోటా - చివరి దశ తెగులు (Late Blight)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఫైటోఫ్తోరా ఇన్ఫెస్టాన్స్ అనే శిలీంధ్రం వల్ల వస్తుంది. చల్లని, తడి వాతావరణంలో పంటను వేగంగా నాశనం చేస్తుంది.",
            "symptoms": "ఆకులు, కాండంపై నల్లటి నీటి మచ్చలు ఏర్పడి మొక్క మొత్తం కుళ్ళిపోతుంది.",
            "treatment": "సైమోక్సానిల్ లేదా మెటలాక్సిల్ + మాంకోజెబ్ తక్షణమే పిచికారీ చేయాలి.",
            "organic": "బోర్డో మిశ్రమం పిచికారీ చేయాలి; తెగులు సోకిన మొక్కలను కాల్చివేయాలి.",
            "prevention": "తేమ ఎక్కువగా ఉండకుండా చూసుకోవాలి."
        }
    },
    "Tomato - Septoria Leaf Spot": {
        "en": {
            "name": "Tomato - Septoria Leaf Spot",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "The fungus Septoria lycopersici can live on horsenettle weeds and old tomato plants, then spread in rain splashes.",
            "symptoms": "Numerous small circular spots (1-3 mm) with dark brown borders and light gray/tan centers speckled with tiny black fruiting bodies.",
            "treatment": "Apply Chlorothalonil or Mancozeb sprays beginning at early fruit cluster formation.",
            "organic": "Remove affected lower leaves. Use liquid copper spray as directed and cover the soil around the plant.",
            "prevention": "Avoid handling wet tomato foliage; practice strict weed control around plots; 2-year crop rotation."
        },
        "hi": {
            "name": "टमाटर - सेप्टोरिया पत्ती धब्बा (Septoria Leaf Spot)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "सेप्टोरिया लाइकोपरसिकी फफूंद। पुरानी पत्तियों और खरपतवारों में रहता है और बारिश की बूंदों से फैलता है।",
            "symptoms": "पत्तियों पर असंख्य छोटे गोल धब्बे (1-3 मिमी) जिनके किनारे गहरे भूरे और केंद्र में हल्का धूसर रंग होता है।",
            "treatment": "क्लोरोथैलोनिल या मैंकोजेब का छिड़काव करें।",
            "organic": "संक्रमित निचली पत्तियों को तोड़ें; कॉपर फफूंदनाशक का छिड़काव करें; मल्चिंग करें।",
            "prevention": "गीले पौधों को न छुएं; खेत में खरपतवार न पनपने दें और 2 साल का फसल चक्र रखें।"
        },
        "te": {
            "name": "టమోటా - సెప్టోరియా ఆకుమచ్చ తెగులు",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "సెప్టోరియా లైకోపెర్సికి శిలీంధ్రం వల్ల వస్తుంది. వర్షపు తుంపర్ల ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై చిన్న చిన్న గుండ్రని మచ్చలు (మధ్యలో బూడిద రంగు, చుట్టూ ముదురు గోధుమ రంగు) ఏర్పడతాయి.",
            "treatment": "క్లోరోథలోనిల్ లేదా మాంకోజెబ్ మందును పిచికారీ చేయాలి.",
            "organic": "తెగులు సోకిన ఆకులను తీసివేయాలి; కాపర్ పిచికారీ చేయాలి.",
            "prevention": "పొలంలో కలుపు లేకుండా చూసుకోవాలి; మొక్కలను తడి ఉన్నప్పుడు తాకకూడదు."
        }
    },
    "Tomato - Yellow Leaf Curl Virus": {
        "en": {
            "name": "Tomato - Yellow Leaf Curl Virus",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Tomato yellow leaf curl virus (TYLCV) spreads from plant to plant through silverleaf whiteflies (Bemisia tabaci).",
            "symptoms": "Leaves curl upward, turn yellow at the edges, and become thick. Plants stay small and flowers may fall off.",
            "treatment": "There is no cure for the virus. Control whiteflies with Imidacloprid, Acetamiprid, or Spirotetramat, following the product label.",
            "organic": "Install yellow sticky cards; spray neem oil (10,000 ppm) or insecticidal soap; remove and bag infected plants.",
            "prevention": "Use 50-mesh insect-proof netting in nurseries; grow resistant tomato varieties (e.g., Tygress, Grandela)."
        },
        "hi": {
            "name": "टमाटर - पीला पत्ती मरोड़ वायरस (Yellow Leaf Curl Virus)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "बेगोमोवायरस (TYLCV)। यह सफेद मक्खी (Whitefly) कीट द्वारा फैलता है।",
            "symptoms": "पत्तियां ऊपर की ओर मुड़ना (कटोरीनुमा), किनारों से पीला पड़ना, पौधे का कद छोटा रह जाना और फूल गिरना।",
            "treatment": "वायरस का कोई सीधा इलाज नहीं है। सफेद मक्खी को मारने के लिए इमिडाक्लोप्रिड या एसिटामिप्रिड का छिड़काव करें।",
            "organic": "पीले चिपचिपे कार्ड (Yellow Sticky Traps) लगाएं; नीम का तेल स्प्रे करें; रोगग्रस्त पौधों को उखाड़कर नष्ट करें।",
            "prevention": "नर्सरी में 50-मेश जाली का उपयोग करें; वायरस-प्रतिरोधी किस्मों की बुवाई करें।"
        },
        "te": {
            "name": "టమోటా - ఆకు ముడుత వైరస్ (Yellow Leaf Curl)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "తెల్లదోమ (వైట్‌ఫ్లై) ద్వారా వ్యాపించే వైరస్ తెగులు.",
            "symptoms": "ఆకులు పైకి దోనె వలె ముడుచుకుపోవడం, పసుపు రంగులోకి మారడం, మొక్క ఎదుగుదల ఆగిపోవడం.",
            "treatment": "వైరస్ నివారణకు మందులు లేవు. తెల్లదోమ నివారణకు ఇమిడాక్లోప్రిడ్ పిచికారీ చేయాలి.",
            "organic": "పసుపు జిగురు అట్టలను ఏర్పాటు చేయాలి; వేప నూనెను పిచికారీ చేయాలి; తెగులు సోకిన మొక్కలను పీకివేయాలి.",
            "prevention": "తెగులును తట్టుకునే రకాలను నాటాలి; నర్సరీ దశలో రక్షణ వలలను వాడాలి."
        }
    },
    "Blueberry - Healthy": {
        "en": {
            "name": "Blueberry - Healthy",
            "crop": "Blueberry",
            "status": "Healthy",
            "cause": "No disease was found. The leaves look normal and healthy.",
            "symptoms": "Vibrant foliage, robust shoots, normal leaf turgor and color.",
            "treatment": "No treatment required. Maintain acidic soil (pH 4.5-5.5) and adequate pine bark or peat mulch.",
            "organic": "Compost with ericaceous mulch, rainwater irrigation.",
            "prevention": "Annual pruning of oldest stems and consistent soil moisture."
        },
        "hi": {
            "name": "ब्लूबेरी - स्वस्थ (Healthy)",
            "crop": "ब्लूबेरी",
            "status": "स्वस्थ",
            "cause": "पौधा पूरी तरह स्वस्थ है।",
            "symptoms": "चमकदार हरी पत्तियां और मजबूत विकास।",
            "treatment": "किसी उपचार की आवश्यकता नहीं है। मिट्टी का pH 4.5-5.5 बनाए रखें।",
            "organic": "अम्लीय कम्पोस्ट और पाइन छाल का उपयोग करें।",
            "prevention": "नियमित छंटाई और उचित नमी बनाए रखें।"
        },
        "te": {
            "name": "బ్లూబెర్రీ - ఆరోగ్యకరమైనది",
            "crop": "బ్లూబెర్రీ",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "మొక్క ఆరోగ్యంగా ఉంది, ఎలాంటి తెగులు లేదు.",
            "symptoms": "ఆకులు పచ్చగా, బలంగా ఉన్నాయి.",
            "treatment": "చికిత్స అవసరం లేదు. నేల pH 4.5-5.5 ఉండేలా చూసుకోవాలి.",
            "organic": "సేంద్రియ ఎరువులు మరియు తగినంత తేమ అందించాలి.",
            "prevention": "ఎండిన కొమ్మలను తొలగించి క్రమబద్ధమైన నీటిపారుదల చేయాలి."
        }
    },
    "Orange - Huanglongbing (Citrus Greening)": {
        "en": {
            "name": "Orange - Huanglongbing (Citrus Greening)",
            "crop": "Orange",
            "status": "Diseased",
            "cause": "The bacterium Candidatus Liberibacter asiaticus spreads through the Asian citrus psyllid insect (Diaphorina citri).",
            "symptoms": "Leaves show uneven yellow patches. Fruits may be small, lopsided, and bitter, with green color at the base. Twigs may die back.",
            "treatment": "There is no cure once a tree is infected. Control Asian citrus psyllid insects using Thiamethoxam or Imidacloprid as directed on the label.",
            "organic": "Remove and destroy infected trees immediately; spray horticultural mineral oils; release Tamarixia radiata parasitoid wasps.",
            "prevention": "Plant certified disease-free nursery stock and establish protective windbreaks."
        },
        "hi": {
            "name": "संतरा - सिट्रस ग्रीनिंग (Huanglongbing)",
            "crop": "संतरा",
            "status": "रोगग्रस्त",
            "cause": "कैंडिडेटस लिबेरीबैक्टर जीवाणु। यह एशियाई सिट्रस सिलिड कीट द्वारा फैलता है।",
            "symptoms": "पत्तियों की नसों पर असमान पीलापन, फल छोटे और कड़वे रहना, टहनियां सूखना।",
            "treatment": "बीमारी का कोई सीधा इलाज नहीं है। वाहक सिलिड कीट को नियंत्रित करने के लिए थियामेथोक्सम का छिड़काव करें।",
            "organic": "संक्रमित पेड़ों को काटकर जलाएं; नीम तेल व मिनरल ऑयल स्प्रे करें।",
            "prevention": "प्रमाणित रोगमुक्त पौधे लगाएं और नियमित निगरानी करें।"
        },
        "te": {
            "name": "నారింజ - సిట్రస్ గ్రీనింగ్ తెగులు",
            "crop": "నారింజ",
            "status": "తెగులు బారిన పడింది",
            "cause": "సిట్రస్ సిల్లిడ్ అనే కీటం ద్వారా వ్యాపించే బ్యాక్టీరియా తెగులు.",
            "symptoms": "ఆకుల ఈనెల మధ్య పసుపు పచ్చని మచ్చలు, కాయలు వంకరగా మారి చేదుగా ఉండడం.",
            "treatment": "ఈ తెగులుకు నివారణ లేదు. సిల్లిడ్ కీటకాల నివారణకు థయామెథోక్సామ్ పిచికారీ చేయాలి.",
            "organic": "బాధిత చెట్లను తీసివేసి నాశనం చేయాలి; వేప నూనె వాడాలి.",
            "prevention": "ధృవీకరించబడిన ఆరోగ్యకరమైన మొక్కలను మాత్రమే నాటాలి."
        }
    },
    "Raspberry - Healthy": {
        "en": {
            "name": "Raspberry - Healthy",
            "crop": "Raspberry",
            "status": "Healthy",
            "cause": "No disease was found. The plant is growing well.",
            "symptoms": "The leaves are deep green and the stems are strong, with no marks or color changes.",
            "treatment": "No treatment needed. Support the canes and water regularly.",
            "organic": "Apply composted wood chips, ensure good air circulation.",
            "prevention": "After harvest, cut out the canes that have already produced fruit."
        },
        "hi": {
            "name": "रास्पबेरी - स्वस्थ (Healthy)",
            "crop": "रास्पबेरी",
            "status": "स्वस्थ",
            "cause": "पौधा पूरी तरह स्वस्थ है।",
            "symptoms": "गहरी हरी पत्तियां और मजबूत शाखाएं।",
            "treatment": "किसी उपचार की आवश्यकता नहीं है।",
            "organic": "उचित कम्पोस्ट और मल्चिंग करें।",
            "prevention": "फसल के बाद पुरानी टहनियों की छंटाई करें।"
        },
        "te": {
            "name": "రాస్ప్బెర్రీ - ఆరోగ్యకరమైనది",
            "crop": "రాస్ప్బెర్రీ",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎలాంటి తెగులు సోకలేదు.",
            "symptoms": "పచ్చని ఆరోగ్యవంతమైన ఆకులు మరియు కాండం.",
            "treatment": "చికిత్స అవసరం లేదు.",
            "organic": "సేంద్రియ ఎరువులు వేయాలి.",
            "prevention": "పాత కొమ్మలను తొలగించాలి."
        }
    },
    "Soybean - Healthy": {
        "en": {
            "name": "Soybean - Healthy",
            "crop": "Soybean",
            "status": "Healthy",
            "cause": "No disease was found. The crop looks healthy and is growing well.",
            "symptoms": "The leaves grow in groups of three and the plant is growing well, with healthy-looking roots.",
            "treatment": "No treatment needed.",
            "organic": "Treat seeds with Rhizobium culture before planting.",
            "prevention": "Rotate with corn or grasses."
        },
        "hi": {
            "name": "सोयाबीन - स्वस्थ (Healthy)",
            "crop": "सोयाबीन",
            "status": "स्वस्थ",
            "cause": "फसल पूर्णतः स्वस्थ है।",
            "symptoms": "समान हरी पत्तियां और स्वस्थ विकास।",
            "treatment": "उपचार की आवश्यकता नहीं।",
            "organic": "राइजोबियम कल्चर का उपयोग करें।",
            "prevention": "मक्का या ज्वार के साथ फसल चक्र अपनाएं।"
        },
        "te": {
            "name": "సోయాబీన్ - ఆరోగ్యకరమైనది",
            "crop": "సోయాబీన్",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "మొక్క ఆరోగ్యంగా ఉంది.",
            "symptoms": "ఆకులు ఆరోగ్యంగా, పచ్చగా ఉన్నాయి.",
            "treatment": "చికిత్స అవసరం లేదు.",
            "organic": "రైజోబియం వాడాలి.",
            "prevention": "పంట మార్పిడి పాటించాలి."
        }
    },
    "Squash - Powdery Mildew": {
        "en": {
            "name": "Squash - Powdery Mildew",
            "crop": "Squash",
            "status": "Diseased",
            "cause": "The fungus Podosphaera xanthii causes this disease. It spreads in warm, dry weather when plants are crowded and shaded.",
            "symptoms": "White talcum-powder-like fungal patches on upper and lower leaf surfaces, leading to yellowing and premature drying.",
            "treatment": "Apply Azoxystrobin, Triflumizole, or Myclobutanil at first sign of white spots.",
            "organic": "Spray potassium bicarbonate (3g/L), diluted milk spray (40% milk, 60% water), or neem oil.",
            "prevention": "Choose resistant squash varieties and increase plant spacing for airflow."
        },
        "hi": {
            "name": "कद्दू/लौकी - चूर्णी फफूंद (Powdery Mildew)",
            "crop": "कद्दू/लौकी",
            "status": "रोगग्रस्त",
            "cause": "पोडोस्फेरा जैन्थी फफूंद। गर्म और शुष्क मौसम में तेजी से पनपता है।",
            "symptoms": "पत्तियों पर सफेद पाउडर जैसे धब्बे, पत्तियां पीली पड़कर सूखना।",
            "treatment": "एज़ोक्सीस्ट्रोबिन (Azoxystrobin) या माइक्लोबुटानिल का छिड़काव करें।",
            "organic": "पोटेशियम बाइकार्बोनेट या नीम के तेल (3%) का स्प्रे करें।",
            "prevention": "पौधों के बीच पर्याप्त दूरी रखें ताकि धूप और हवा मिले।"
        },
        "te": {
            "name": "గుమ్మడి/దోస - బూడిద తెగులు (Powdery Mildew)",
            "crop": "గుమ్మడి",
            "status": "తెగులు బారిన పడింది",
            "cause": "పోడోస్ఫెరా జాంతి శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై బూడిద వంటి తెల్లని పొర ఏర్పడి ఆకులు ఎండిపోతాయి.",
            "treatment": "అజోక్సిస్ట్రోబిన్ లేదా మైక్లోబ్యుటానిల్ పిచికారీ చేయాలి.",
            "organic": "పొటాషియం బైకార్బోనేట్ లేదా వేప నూనె పిచికారీ చేయాలి.",
            "prevention": "మొక్కల మధ్య తగినంత గాలి వెలుతురు ఉండేలా నాటాలి."
        }
    },
    "Tomato - Leaf Mold": {
        "en": {
            "name": "Tomato - Leaf Mold",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "The fungus Passalora fulva (Cladosporium fulvum) causes this disease. It spreads easily in very humid greenhouses (over 85% humidity).",
            "symptoms": "Pale green to yellowish spots on upper leaf surfaces, with olive-green to grayish velvety mold on the undersides.",
            "treatment": "Apply Chlorothalonil, Mancozeb, or Copper sulfate at early symptoms.",
            "organic": "Use a leaf spray containing Bacillus amyloliquefaciens as directed. Let more fresh air into the greenhouse.",
            "prevention": "Maintain relative humidity below 80% and avoid overhead watering."
        },
        "hi": {
            "name": "टमाटर - पत्ती का फफूंद (Leaf Mold)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "क्लैडोस्पोरियम फफूंद। अत्यधिक नमी (>85%) और पॉलीहाउस में तेजी से फैलता है।",
            "symptoms": "पत्तियों की ऊपरी सतह पर पीले धब्बे और निचली सतह पर जैतून जैसा मखमली फफूंद।",
            "treatment": "क्लोरोथैलोनिल या मैंकोजेब का छिड़काव करें।",
            "organic": "ग्रीनहाउस में वेंटिलेशन बढ़ाएं; कॉपर कवकनाशी स्प्रे करें।",
            "prevention": "नमी 80% से कम रखें और ड्रिप सिंचाई का उपयोग करें।"
        },
        "te": {
            "name": "టమోటా - ఆకు బూజు తెగులు (Leaf Mold)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "పాసలోరా ఫుల్వా శిలీంధ్రం వల్ల వస్తుంది. అధిక తేమ ఉన్నప్పుడు వ్యాపిస్తుంది.",
            "symptoms": "ఆకుల పైభాగంలో పసుపు మచ్చలు, అడుగు భాగంలో ఆలివ్ ఆకుపచ్చ రంగు బూజు.",
            "treatment": "క్లోరోథలోనిల్ లేదా మాంకోజెబ్ మందును పిచికారీ చేయాలి.",
            "organic": "గాలి వెలుతురు పెంచాలి; కాపర్ పిచికారీ చేయాలి.",
            "prevention": "పంటలో అధిక తేమ లేకుండా చూసుకోవాలి."
        }
    },
    "Tomato - Spider Mites (Two-spotted spider mite)": {
        "en": {
            "name": "Tomato - Spider Mites (Two-spotted spider mite)",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Tetranychus urticae (Arachnid mite pest). Proliferates rapidly under hot, dry, dusty conditions.",
            "symptoms": "Fine yellow-white stippling on leaf surfaces, bronzing and drying of leaves, and visible fine webbing covering shoots.",
            "treatment": "Apply acaricides/miticides such as Abamectin, Bifenazate, or Spiromesifen.",
            "organic": "Spray insecticidal soap, rosemary oil, or neem oil; introduce predatory mites (Phytoseiulus persimilis).",
            "prevention": "Keep soil adequately watered; wash dust off field foliage regularly."
        },
        "hi": {
            "name": "टमाटर - लाल मकड़ी (Spider Mites)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "टेट्रानिचस अर्टिके (Spider Mite)। गर्म, शुष्क और धूल भरे मौसम में तेजी से बढ़ता है।",
            "symptoms": "पत्तियों पर पीले-सफेद बारीक बिंदु (Stippling), पत्तियों पर बारीक जाले और पत्तियों का सूखना।",
            "treatment": "एबामेक्टिन (Abamectin) या स्पाइरोमेसिफेन माइटिसाइड का छिड़काव करें।",
            "organic": "नीम का तेल (5 मिली/लीटर) या साबुन के घोल का छिड़काव करें।",
            "prevention": "खेत को नम रखें और धूल जमा न होने दें।"
        },
        "te": {
            "name": "టమోటా - నల్లి/సాలీడు పురుగు (Spider Mites)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఎర్ర నల్లి లేదా సాలీడు పురుగు ఆకుల రసాన్ని పీల్చడం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై చిన్న చిన్న పసుపు రంగు చుక్కలు, ఆకుల అడుగున సన్నని తెల్లని బూజు/జాలాలు.",
            "treatment": "అబామెక్టిన్ లేదా స్పైరోమెసిఫెన్ పిచికారీ చేయాలి.",
            "organic": "వేప నూనె లేదా సబ్బు ద్రావణం పిచికారీ చేయాలి.",
            "prevention": "పొలంలో దుమ్ము లేకుండా మరియు తగినంత తేమ ఉంచాలి."
        }
    },
    "Tomato - Target Spot": {
        "en": {
            "name": "Tomato - Target Spot",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "The fungus Corynespora cassiicola spreads in warm, humid weather in tropical and subtropical areas.",
            "symptoms": "Small brown spots appear on the leaves and grow into rings like a target.",
            "treatment": "Apply Azoxystrobin + Difenoconazole or Boscalid + Pyraclostrobin.",
            "organic": "Spray copper hydroxide or Bacillus subtilis on the leaves as directed. Remove affected lower leaves.",
            "prevention": "Leave enough space between rows so plants dry after rain. Avoid watering from above."
        },
        "hi": {
            "name": "टमाटर - टारगेट स्पॉट (Target Spot)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "कोरीनेस्पोरा कैसीकोला फफूंद। गर्म और अत्यधिक आर्द्र मौसम में फैलता है।",
            "symptoms": "पत्तियों पर लक्ष्य (Bullseye/Target) जैसे गोल चक्राकार भूरे धब्बे, पत्तियां गिरना।",
            "treatment": "एज़ोक्सीस्ट्रोबिन या पाइराक्लोस्ट्रोबिन कवकनाशी का छिड़काव करें।",
            "organic": "कॉपर हाइड्रोक्साइड या बैसिलस सबटिलिस का छिड़काव करें; निचली रोगग्रस्त पत्तियों को हटाएं।",
            "prevention": "पौधों के बीच दूरी रखें और टपक सिंचाई करें।"
        },
        "te": {
            "name": "టమోటా - టార్గెట్ స్పాట్ (లక్ష్యపు మచ్చ తెగులు)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "కోరినెస్‌స్పోరా కాసికోలా శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై చక్రాల వంటి గుండ్రని ముదురు గోధుమ రంగు మచ్చలు (టార్గెట్ బోర్డు వలె).",
            "treatment": "అజోక్సిస్ట్రోబిన్ లేదా మాంకోజెబ్ పిచికారీ చేయాలి.",
            "organic": "కాపర్ హైడ్రాక్సైడ్ స్ప్రే చేయాలి.",
            "prevention": "పైనుండి నీరు పోయకుండా డ్రిప్ పద్ధతి వాడాలి."
        }
    },
    "Tomato - Tomato Mosaic Virus": {
        "en": {
            "name": "Tomato - Tomato Mosaic Virus",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Tomato mosaic virus (ToMV) can remain on hands and tools and spread through touch or infected seeds.",
            "symptoms": "Leaves show a mix of light and dark green patches and may become narrow or misshapen.",
            "treatment": "There is no cure for the virus. Clean tools with 20% skim milk or 10% trisodium phosphate (TSP) before using them on healthy plants.",
            "organic": "Immediately rogue and burn infected plants; wash hands thoroughly before touching healthy plants.",
            "prevention": "Use certified virus-free seeds and tomato varieties that can withstand the disease. Do not handle plants after using tobacco unless you have washed your hands."
        },
        "hi": {
            "name": "टमाटर - मोजेक वायरस (Tomato Mosaic Virus)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "टोबामोवायरस (ToMV)। यह हाथों, औजारों और संक्रमित बीजों के माध्यम से आसानी से फैलता है।",
            "symptoms": "पत्तियों पर हल्के और गहरे हरे रंग के मोजेक जैसे धब्बे, पत्तियां विकृत होना।",
            "treatment": "वायरस का कोई इलाज नहीं है। औजारों को ट्राइसोडियम फॉस्फेट या दूध के घोल से साफ करें।",
            "organic": "संक्रमित पौधों को उखाड़कर तुरंत नष्ट करें; हाथों को साबुन से धोएं।",
            "prevention": "रोग-प्रतिरोधी बीज लगाएं; तंबाकू का उपयोग करने वालों को पौधों को छूने न दें।"
        },
        "te": {
            "name": "టమోటా - మొజాయిక్ వైరస్ తెగులు",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "టోబామోవైరస్ వల్ల వస్తుంది. తాకడం, పనిముట్లు మరియు విత్తనాల ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై లేత మరియు ముదురు ఆకుపచ్చని చారల మచ్చలు, ఆకులు సన్నగా ముడుచుకుపోవడం.",
            "treatment": "చికిత్స లేదు. పనిముట్లను క్రిమిసంహారక ద్రావణంతో కడగాలి.",
            "organic": "తెగులు సోకిన మొక్కలను తీసివేసి తగులబెట్టాలి.",
            "prevention": "వైరస్ లేని విత్తనాలను వాడాలి మరియు తోటలో ధూమపానం చేయకూడదు."
        }
    }
}


def get_ui_text(key: str, lang: str = "en") -> str:
    """Retrieve UI string by key in requested language with English fallback."""
    lang_dict = STRINGS.get(lang, STRINGS["en"])
    return lang_dict.get(key, STRINGS["en"].get(key, key))


def get_crop_translation(crop_name: str, lang: str = "en") -> dict:
    """Retrieve translated crop details."""
    crop_key = crop_name.lower().strip()
    crop_info = CROPS_I18N.get(crop_key, {})
    
    if not crop_info:
        return {
            "name": crop_name.title(),
            "season": "Season data not available.",
            "soil": "Soil data not available.",
            "care": "Water regularly and use a balanced fertilizer."
        }
    
    return crop_info.get(lang, crop_info.get("en", {
        "name": crop_name.title(),
        "season": "Season data not available.",
        "soil": "Soil data not available.",
        "care": "Water regularly and use a balanced fertilizer."
    }))


def get_disease_translation(disease_name: str, lang: str = "en") -> dict:
    """Retrieve translated disease details with fallback."""
    disease_info = DISEASES_I18N.get(disease_name, {})
    
    if not disease_info:
        # Case-insensitive fallback lookup
        for d_key, data in DISEASES_I18N.items():
            if d_key.lower() == disease_name.lower():
                disease_info = data
                break
                
    if not disease_info:
        is_healthy = "healthy" in disease_name.lower()
        return {
            "name": disease_name,
            "crop": disease_name.split(" - ")[0] if " - " in disease_name else "Plant",
            "status": "Healthy" if is_healthy else "Diseased",
            "cause": "No disease was found." if is_healthy else "The cause of the disease has not yet been confirmed.",
            "symptoms": "Clean foliage." if is_healthy else "Visible leaf abnormalities observed.",
            "treatment": "No treatment required." if is_healthy else "Consult local agricultural extension.",
            "organic": "Maintain balanced organic nutrition." if is_healthy else "Use neem-based bio-pesticide.",
            "prevention": "Check plants regularly and use balanced fertilizer."
        }
        
    return disease_info.get(lang, disease_info.get("en", {}))
