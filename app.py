import streamlit as st
import re

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Unlock Your Phone | Gesner Deslandes",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# TRANSLATIONS DICTIONARY
# =========================================================
T = {
    "en": {
        "lang_label": "🌐 Language",
        "hero_subtitle": "📱 Unlock Your Phone Application",
        "hero_role": "Software Engineer · Engineer-in-Chief, GlobalInternet.py",
        "intro_title": "Welcome to the Unlock Your Phone Application",
        "intro_text": "a professional, all-in-one assistant for legitimate phone diagnostics and carrier unlock requests.",
        "intro_helps": "This tool helps you:",
        "intro_li1": "Validate any phone's IMEI number using the international Luhn algorithm",
        "intro_li2": "Look up device specifications by brand and model",
        "intro_li3": "Generate the official carrier unlock request to send to Digicel, Natcom, or any carrier",
        "intro_li4": "Get direct 1-on-1 consultation with Gesner for advanced troubleshooting",
        "intro_warn": "⚠️ Important: This app only supports legitimate phone operations. We do NOT bypass lock screens, FRP locks, iCloud activation locks, or any security feature. All services require proof of device ownership.",
        "services_title": "🛠️ Our Services",
        "svc1_title": "IMEI Validator",
        "svc1_desc": "Check if an IMEI is mathematically valid using the official Luhn algorithm used by every carrier worldwide.",
        "svc2_title": "Device Lookup",
        "svc2_desc": "Look up device specs by brand and model. Get processor info, storage options, and OS guidance.",
        "svc3_title": "Carrier Unlock",
        "svc3_desc": "Generate a professional unlock request to send to your carrier (Digicel, Natcom, AT&T, etc.).",
        "svc4_title": "Consultation",
        "svc4_desc": "Talk 1-on-1 with Gesner via WhatsApp for advanced phone troubleshooting and repair guidance.",
        "imei_title": "🔍 IMEI Validator",
        "imei_input_label": "Enter your 15-digit IMEI number",
        "imei_input_placeholder": "e.g. 358751234567890",
        "imei_help": "Dial *#06# on your phone to see your IMEI.",
        "imei_btn": "✅ Validate IMEI",
        "imei_len_err": "❌ IMEI must be exactly 15 digits.",
        "imei_valid": "✅ Valid IMEI",
        "imei_valid_msg": "This IMEI passes the Luhn checksum used by all carriers worldwide. You can safely include it in your carrier unlock request below.",
        "imei_invalid": "❌ Invalid IMEI",
        "imei_invalid_msg": "This IMEI fails the Luhn checksum. Please re-check the number — dial *#06# on your phone to see the correct IMEI.",
        "device_title": "📋 Device Lookup",
        "device_brand": "Brand",
        "device_model": "Model",
        "device_btn": "🔎 Look Up Device",
        "device_not_found": "❌ Device not found in our database. Please contact Gesner for a custom lookup.",
        "unlock_title": "🔓 Carrier Unlock Assistant",
        "unlock_intro": "Fill in the details below. The app will generate a professional unlock request email that you can send directly to your carrier (Digicel, Natcom, AT&T, T-Mobile, etc.). This is the only legal path to remove a carrier SIM lock.",
        "unlock_name": "Your Full Name",
        "unlock_name_ph": "e.g. Jean Baptiste",
        "unlock_email": "Your Email Address",
        "unlock_email_ph": "you@example.com",
        "unlock_carrier": "Your Carrier",
        "unlock_imei": "Device IMEI (15 digits)",
        "unlock_imei_ph": "358751234567890",
        "unlock_device": "Device Model",
        "unlock_device_ph": "e.g. iPhone 12, Galaxy S21",
        "unlock_reason": "Reason for unlock request",
        "unlock_reason_ph": "I am the original owner of this device and I want to use it with another carrier.",
        "unlock_btn": "📧 Generate Unlock Request Email",
        "unlock_fill_all": "❌ Please fill in all fields before generating the email.",
        "unlock_bad_imei": "❌ The IMEI you entered is not valid. Please check it and try again.",
        "unlock_ready": "✅ Your unlock request email is ready. Copy it below and send it to your carrier.",
        "consult_title": "💬 Personal Consultation with Gesner",
        "consult_intro": "Need direct 1-on-1 help with a specific phone issue? Book a personal consultation with Gesner. He will guide you through the process over WhatsApp — step by step, in Kreyòl or English.",
        "consult_includes": "Consultation includes:",
        "consult_li1": "Personalized diagnosis of your phone issue",
        "consult_li2": "Detailed walkthrough for legitimate fixes",
        "consult_li3": "Carrier unlock guidance specific to your device",
        "consult_li4": "Follow-up support for 7 days",
        "moncash_label": "💳 MonCash Payment",
        "moncash_amount": "Send $5 USD · ~700 HTG",
        "moncash_note": "Open MonCash → Transfer → Prisme → Prisme. Enter the number above → Confirm $5 → Copy your transaction reference",
        "consult_name": "Your Name",
        "consult_name_ph": "Full name",
        "consult_phone": "Your WhatsApp Number",
        "consult_phone_ph": "+509 XXXX XXXX",
        "consult_ref": "MonCash Transaction Reference",
        "consult_ref_ph": "e.g. MC987654321",
        "consult_issue": "Your Phone Issue (short)",
        "consult_issue_ph": "e.g. Cannot unlock carrier",
        "consult_notes": "Tell Gesner more about your issue",
        "consult_notes_ph": "Describe what you need help with…",
        "consult_btn": "📩 Submit Consultation Request",
        "consult_fill": "❌ Please fill in your name, WhatsApp number, and MonCash reference.",
        "consult_thanks": "✅ Thank you,",
        "consult_received": "Your consultation request has been received.",
        "consult_contact": "Gesner will contact you on WhatsApp within 24 hours at",
        "consult_ref_label": "Your MonCash reference:",
        "consult_urgent": "For urgent matters, call",
        "consult_directly": "directly.",
        "safety_title": "🛡️ Trust & Safety",
        "safety_notdo": "⚠️ What this app does NOT do:",
        "safety_not1": "Does NOT bypass lock screens (PIN, pattern, password)",
        "safety_not2": "Does NOT bypass iCloud activation locks",
        "safety_not3": "Does NOT bypass Google FRP (Factory Reset Protection)",
        "safety_not4": "Does NOT bypass any manufacturer or owner security feature",
        "safety_do": "✅ What this app DOES do:",
        "safety_do1": "Validate IMEI numbers (Luhn algorithm)",
        "safety_do2": "Look up legitimate device specifications",
        "safety_do3": "Generate carrier unlock request emails",
        "safety_do4": "Connect you to a certified technician for consultation",
        "safety_protection": "For your protection: We require proof of ownership for all services. Any attempt to use this app to bypass security on a device you do not own is strictly forbidden and may be illegal.",
        "footer_role": "Software Engineer · Engineer-in-Chief, GlobalInternet.py",
        "footer_built": "© 2026 Unlock Your Phone Application · Built with Streamlit",
        "unlock_subject": "Subject: Carrier Unlock Request — IMEI",
        "unlock_dear": "Dear",
        "unlock_support": "Customer Support,",
        "unlock_body1": "I am writing to formally request a SIM network unlock for my device. I am the original owner and I have fulfilled all contractual obligations associated with this device.",
        "unlock_body2": "Please find the details below:",
        "unlock_owner_name": "Owner Name:",
        "unlock_owner_email": "Owner Email:",
        "unlock_device_model": "Device Model:",
        "unlock_imei_label": "IMEI:",
        "unlock_carrier_label": "Carrier:",
        "unlock_reason_label": "Reason for request:",
        "unlock_reason_default": "I want to use this device with a different carrier network.",
        "unlock_attached": "I have attached my proof of purchase and a copy of my ID for verification. Please process this unlock request at your earliest convenience and let me know the expected turnaround time and any additional requirements.",
        "unlock_thanks": "Thank you for your time and assistance.",
        "unlock_sincerely": "Sincerely,",
    },
    "fr": {
        "lang_label": "🌐 Langue",
        "hero_subtitle": "📱 Application Déverrouillez Votre Téléphone",
        "hero_role": "Ingénieur Logiciel · Ingénieur-en-Chef, GlobalInternet.py",
        "intro_title": "Bienvenue dans l'Application Déverrouillez Votre Téléphone",
        "intro_text": "un assistant professionnel tout-en-un pour le diagnostic légitime de téléphones et les demandes de déverrouillage d'opérateur.",
        "intro_helps": "Cet outil vous aide à :",
        "intro_li1": "Valider le numéro IMEI de tout téléphone avec l'algorithme Luhn international",
        "intro_li2": "Rechercher les spécifications d'un appareil par marque et modèle",
        "intro_li3": "Générer la demande officielle de déverrouillage à envoyer à Digicel, Natcom ou tout opérateur",
        "intro_li4": "Obtenir une consultation directe 1-à-1 avec Gesner pour un dépannage avancé",
        "intro_warn": "⚠️ Important : Cette application ne prend en charge que les opérations légitimes. Nous ne contournons PAS les écrans de verrouillage, les verrous FRP, les verrous d'activation iCloud, ni aucune fonction de sécurité. Tous les services exigent une preuve de propriété de l'appareil.",
        "services_title": "🛠️ Nos Services",
        "svc1_title": "Validateur IMEI",
        "svc1_desc": "Vérifiez si un IMEI est mathématiquement valide avec l'algorithme Luhn officiel utilisé par tous les opérateurs dans le monde.",
        "svc2_title": "Recherche d'Appareil",
        "svc2_desc": "Recherchez les spécifications d'un appareil par marque et modèle. Obtenez les infos processeur, stockage et OS.",
        "svc3_title": "Déverrouillage Opérateur",
        "svc3_desc": "Générez une demande professionnelle de déverrouillage à envoyer à votre opérateur (Digicel, Natcom, AT&T, etc.).",
        "svc4_title": "Consultation",
        "svc4_desc": "Parlez 1-à-1 avec Gesner via WhatsApp pour un dépannage avancé et des conseils de réparation.",
        "imei_title": "🔍 Validateur IMEI",
        "imei_input_label": "Entrez votre numéro IMEI à 15 chiffres",
        "imei_input_placeholder": "ex. 358751234567890",
        "imei_help": "Composez *#06# sur votre téléphone pour voir votre IMEI.",
        "imei_btn": "✅ Valider l'IMEI",
        "imei_len_err": "❌ L'IMEI doit comporter exactement 15 chiffres.",
        "imei_valid": "✅ IMEI Valide",
        "imei_valid_msg": "Cet IMEI passe la somme de contrôle Luhn utilisée par tous les opérateurs. Vous pouvez l'inclure dans votre demande de déverrouillage ci-dessous.",
        "imei_invalid": "❌ IMEI Invalide",
        "imei_invalid_msg": "Cet IMEI échoue à la somme de contrôle Luhn. Vérifiez le numéro — composez *#06# pour voir le bon IMEI.",
        "device_title": "📋 Recherche d'Appareil",
        "device_brand": "Marque",
        "device_model": "Modèle",
        "device_btn": "🔎 Rechercher l'Appareil",
        "device_not_found": "❌ Appareil non trouvé dans notre base. Contactez Gesner pour une recherche personnalisée.",
        "unlock_title": "🔓 Assistant de Déverrouillage Opérateur",
        "unlock_intro": "Remplissez les détails ci-dessous. L'application générera un e-mail professionnel de demande de déverrouillage que vous pourrez envoyer à votre opérateur (Digicel, Natcom, AT&T, T-Mobile, etc.). C'est le seul chemin légal pour retirer un verrou SIM.",
        "unlock_name": "Votre Nom Complet",
        "unlock_name_ph": "ex. Jean Baptiste",
        "unlock_email": "Votre Adresse E-mail",
        "unlock_email_ph": "vous@exemple.com",
        "unlock_carrier": "Votre Opérateur",
        "unlock_imei": "IMEI de l'Appareil (15 chiffres)",
        "unlock_imei_ph": "358751234567890",
        "unlock_device": "Modèle de l'Appareil",
        "unlock_device_ph": "ex. iPhone 12, Galaxy S21",
        "unlock_reason": "Raison de la demande de déverrouillage",
        "unlock_reason_ph": "Je suis le propriétaire original de cet appareil et je veux l'utiliser avec un autre opérateur.",
        "unlock_btn": "📧 Générer l'E-mail de Demande",
        "unlock_fill_all": "❌ Veuillez remplir tous les champs avant de générer l'e-mail.",
        "unlock_bad_imei": "❌ L'IMEI saisi n'est pas valide. Vérifiez-le et réessayez.",
        "unlock_ready": "✅ Votre e-mail de demande est prêt. Copiez-le ci-dessous et envoyez-le à votre opérateur.",
        "consult_title": "💬 Consultation Personnelle avec Gesner",
        "consult_intro": "Besoin d'aide directe 1-à-1 pour un problème de téléphone ? Réservez une consultation personnelle avec Gesner. Il vous guidera par WhatsApp — étape par étape, en Créole ou en Anglais.",
        "consult_includes": "La consultation comprend :",
        "consult_li1": "Diagnostic personnalisé de votre problème",
        "consult_li2": "Guide détaillé pour des solutions légitimes",
        "consult_li3": "Conseils de déverrouillage spécifiques à votre appareil",
        "consult_li4": "Support de suivi pendant 7 jours",
        "moncash_label": "💳 Paiement MonCash",
        "moncash_amount": "Envoyez 5 $ USD · ~700 HTG",
        "moncash_note": "Ouvrez MonCash → Transfert → Prisme → Prisme. Entrez le numéro ci-dessus → Confirmez 5 $ → Copiez votre référence",
        "consult_name": "Votre Nom",
        "consult_name_ph": "Nom complet",
        "consult_phone": "Votre Numéro WhatsApp",
        "consult_phone_ph": "+509 XXXX XXXX",
        "consult_ref": "Référence de Transaction MonCash",
        "consult_ref_ph": "ex. MC987654321",
        "consult_issue": "Votre Problème (court)",
        "consult_issue_ph": "ex. Impossible de déverrouiller",
        "consult_notes": "Dites-en plus à Gesner sur votre problème",
        "consult_notes_ph": "Décrivez ce dont vous avez besoin…",
        "consult_btn": "📩 Soumettre la Demande",
        "consult_fill": "❌ Veuillez remplir votre nom, numéro WhatsApp et référence MonCash.",
        "consult_thanks": "✅ Merci,",
        "consult_received": "Votre demande de consultation a été reçue.",
        "consult_contact": "Gesner vous contactera sur WhatsApp sous 24 heures au",
        "consult_ref_label": "Votre référence MonCash :",
        "consult_urgent": "Pour les urgences, appelez le",
        "consult_directly": "directement.",
        "safety_title": "🛡️ Confiance & Sécurité",
        "safety_notdo": "⚠️ Ce que cette application NE fait PAS :",
        "safety_not1": "Ne contourne PAS les écrans de verrouillage",
        "safety_not2": "Ne contourne PAS les verrous d'activation iCloud",
        "safety_not3": "Ne contourne PAS le FRP de Google",
        "safety_not4": "Ne contourne AUCUNE fonction de sécurité",
        "safety_do": "✅ Ce que cette application FAIT :",
        "safety_do1": "Valider les numéros IMEI (algorithme Luhn)",
        "safety_do2": "Rechercher les spécifications légitimes",
        "safety_do3": "Générer des e-mails de demande de déverrouillage",
        "safety_do4": "Vous connecter à un technicien certifié",
        "safety_protection": "Pour votre protection : Nous exigeons une preuve de propriété pour tous les services. Toute tentative de contournement de la sécurité sur un appareil que vous ne possédez pas est strictement interdite et peut être illégale.",
        "footer_role": "Ingénieur Logiciel · Ingénieur-en-Chef, GlobalInternet.py",
        "footer_built": "© 2026 Application Déverrouillez Votre Téléphone · Créé avec Streamlit",
        "unlock_subject": "Objet : Demande de Déverrouillage Opérateur — IMEI",
        "unlock_dear": "Cher",
        "unlock_support": "Service Client,",
        "unlock_body1": "Je vous écris pour demander formellement un déverrouillage réseau SIM pour mon appareil. Je suis le propriétaire original et j'ai rempli toutes les obligations contractuelles.",
        "unlock_body2": "Veuillez trouver les détails ci-dessous :",
        "unlock_owner_name": "Nom du Propriétaire :",
        "unlock_owner_email": "E-mail du Propriétaire :",
        "unlock_device_model": "Modèle de l'Appareil :",
        "unlock_imei_label": "IMEI :",
        "unlock_carrier_label": "Opérateur :",
        "unlock_reason_label": "Raison de la demande :",
        "unlock_reason_default": "Je veux utiliser cet appareil avec un autre réseau.",
        "unlock_attached": "J'ai joint ma preuve d'achat et une copie de ma pièce d'identité pour vérification. Veuillez traiter cette demande dès que possible.",
        "unlock_thanks": "Merci pour votre temps et votre assistance.",
        "unlock_sincerely": "Cordialement,",
    },
    "es": {
        "lang_label": "🌐 Idioma",
        "hero_subtitle": "📱 Aplicación Desbloquea Tu Teléfono",
        "hero_role": "Ingeniero de Software · Ingeniero en Jefe, GlobalInternet.py",
        "intro_title": "Bienvenido a la Aplicación Desbloquea Tu Teléfono",
        "intro_text": "un asistente profesional todo en uno para diagnóstico legítimo de teléfonos y solicitudes de desbloqueo de operador.",
        "intro_helps": "Esta herramienta te ayuda a:",
        "intro_li1": "Validar el número IMEI de cualquier teléfono con el algoritmo Luhn internacional",
        "intro_li2": "Buscar especificaciones de dispositivos por marca y modelo",
        "intro_li3": "Generar la solicitud oficial de desbloqueo para Digicel, Natcom o cualquier operador",
        "intro_li4": "Obtener consulta directa 1-a-1 con Gesner para solución avanzada",
        "intro_warn": "⚠️ Importante: Esta aplicación solo admite operaciones legítimas. NO eludimos pantallas de bloqueo, bloqueos FRP, bloqueos de activación de iCloud ni ninguna función de seguridad. Todos los servicios requieren prueba de propiedad del dispositivo.",
        "services_title": "🛠️ Nuestros Servicios",
        "svc1_title": "Validador IMEI",
        "svc1_desc": "Verifica si un IMEI es matemáticamente válido con el algoritmo Luhn oficial usado por todos los operadores del mundo.",
        "svc2_title": "Búsqueda de Dispositivo",
        "svc2_desc": "Busca especificaciones por marca y modelo. Obtén info del procesador, almacenamiento y sistema operativo.",
        "svc3_title": "Desbloqueo de Operador",
        "svc3_desc": "Genera una solicitud profesional de desbloqueo para tu operador (Digicel, Natcom, AT&T, etc.).",
        "svc4_title": "Consulta",
        "svc4_desc": "Habla 1-a-1 con Gesner por WhatsApp para solución avanzada y guía de reparación.",
        "imei_title": "🔍 Validador IMEI",
        "imei_input_label": "Ingresa tu número IMEI de 15 dígitos",
        "imei_input_placeholder": "ej. 358751234567890",
        "imei_help": "Marca *#06# en tu teléfono para ver tu IMEI.",
        "imei_btn": "✅ Validar IMEI",
        "imei_len_err": "❌ El IMEI debe tener exactamente 15 dígitos.",
        "imei_valid": "✅ IMEI Válido",
        "imei_valid_msg": "Este IMEI pasa la suma de verificación Luhn usada por todos los operadores. Puedes incluirlo en tu solicitud de desbloqueo abajo.",
        "imei_invalid": "❌ IMEI Inválido",
        "imei_invalid_msg": "Este IMEI falla la suma de verificación Luhn. Verifica el número — marca *#06# para ver el IMEI correcto.",
        "device_title": "📋 Búsqueda de Dispositivo",
        "device_brand": "Marca",
        "device_model": "Modelo",
        "device_btn": "🔎 Buscar Dispositivo",
        "device_not_found": "❌ Dispositivo no encontrado. Contacta a Gesner para búsqueda personalizada.",
        "unlock_title": "🔓 Asistente de Desbloqueo de Operador",
        "unlock_intro": "Completa los detalles abajo. La app generará un correo profesional de solicitud de desbloqueo que puedes enviar a tu operador (Digicel, Natcom, AT&T, T-Mobile, etc.). Esta es la única vía legal para quitar un bloqueo SIM.",
        "unlock_name": "Tu Nombre Completo",
        "unlock_name_ph": "ej. Juan Bautista",
        "unlock_email": "Tu Correo Electrónico",
        "unlock_email_ph": "tu@ejemplo.com",
        "unlock_carrier": "Tu Operador",
        "unlock_imei": "IMEI del Dispositivo (15 dígitos)",
        "unlock_imei_ph": "358751234567890",
        "unlock_device": "Modelo del Dispositivo",
        "unlock_device_ph": "ej. iPhone 12, Galaxy S21",
        "unlock_reason": "Razón de la solicitud",
        "unlock_reason_ph": "Soy el propietario original y quiero usar este dispositivo con otro operador.",
        "unlock_btn": "📧 Generar Correo de Solicitud",
        "unlock_fill_all": "❌ Por favor completa todos los campos antes de generar el correo.",
        "unlock_bad_imei": "❌ El IMEI ingresado no es válido. Verifícalo e intenta de nuevo.",
        "unlock_ready": "✅ Tu correo de solicitud está listo. Cópialo abajo y envíalo a tu operador.",
        "consult_title": "💬 Consulta Personal con Gesner",
        "consult_intro": "¿Necesitas ayuda directa 1-a-1 con un problema de teléfono? Reserva una consulta personal con Gesner. Te guiará por WhatsApp — paso a paso, en Criollo o Inglés.",
        "consult_includes": "La consulta incluye:",
        "consult_li1": "Diagnóstico personalizado de tu problema",
        "consult_li2": "Guía detallada para soluciones legítimas",
        "consult_li3": "Guía de desbloqueo específica para tu dispositivo",
        "consult_li4": "Soporte de seguimiento por 7 días",
        "moncash_label": "💳 Pago MonCash",
        "moncash_amount": "Envía $5 USD · ~700 HTG",
        "moncash_note": "Abre MonCash → Transferencia → Prisme → Prisme. Ingresa el número arriba → Confirma $5 → Copia tu referencia",
        "consult_name": "Tu Nombre",
        "consult_name_ph": "Nombre completo",
        "consult_phone": "Tu Número de WhatsApp",
        "consult_phone_ph": "+509 XXXX XXXX",
        "consult_ref": "Referencia de Transacción MonCash",
        "consult_ref_ph": "ej. MC987654321",
        "consult_issue": "Tu Problema (corto)",
        "consult_issue_ph": "ej. No puedo desbloquear",
        "consult_notes": "Cuéntale más a Gesner sobre tu problema",
        "consult_notes_ph": "Describe lo que necesitas…",
        "consult_btn": "📩 Enviar Solicitud de Consulta",
        "consult_fill": "❌ Por favor completa tu nombre, WhatsApp y referencia MonCash.",
        "consult_thanks": "✅ ¡Gracias,",
        "consult_received": "Tu solicitud de consulta ha sido recibida.",
        "consult_contact": "Gesner te contactará por WhatsApp en 24 horas al",
        "consult_ref_label": "Tu referencia MonCash:",
        "consult_urgent": "Para casos urgentes, llama al",
        "consult_directly": "directamente.",
        "safety_title": "🛡️ Confianza y Seguridad",
        "safety_notdo": "⚠️ Lo que esta app NO hace:",
        "safety_not1": "NO elude pantallas de bloqueo",
        "safety_not2": "NO elude bloqueos de activación de iCloud",
        "safety_not3": "NO elude FRP de Google",
        "safety_not4": "NO elude ninguna función de seguridad",
        "safety_do": "✅ Lo que esta app SÍ hace:",
        "safety_do1": "Validar números IMEI (algoritmo Luhn)",
        "safety_do2": "Buscar especificaciones legítimas",
        "safety_do3": "Generar correos de solicitud de desbloqueo",
        "safety_do4": "Conectarte con un técnico certificado",
        "safety_protection": "Para tu protección: Requerimos prueba de propiedad para todos los servicios. Cualquier intento de eludir la seguridad en un dispositivo que no posees está estrictamente prohibido y puede ser ilegal.",
        "footer_role": "Ingeniero de Software · Ingeniero en Jefe, GlobalInternet.py",
        "footer_built": "© 2026 Aplicación Desbloquea Tu Teléfono · Hecho con Streamlit",
        "unlock_subject": "Asunto: Solicitud de Desbloqueo de Operador — IMEI",
        "unlock_dear": "Estimado",
        "unlock_support": "Servicio al Cliente,",
        "unlock_body1": "Escribo para solicitar formalmente un desbloqueo de red SIM para mi dispositivo. Soy el propietario original y he cumplido todas las obligaciones contractuales.",
        "unlock_body2": "Detalles a continuación:",
        "unlock_owner_name": "Nombre del Propietario:",
        "unlock_owner_email": "Correo del Propietario:",
        "unlock_device_model": "Modelo del Dispositivo:",
        "unlock_imei_label": "IMEI:",
        "unlock_carrier_label": "Operador:",
        "unlock_reason_label": "Razón de la solicitud:",
        "unlock_reason_default": "Quiero usar este dispositivo con otra red.",
        "unlock_attached": "He adjuntado prueba de compra y copia de mi ID para verificación. Por favor procese esta solicitud lo antes posible.",
        "unlock_thanks": "Gracias por su tiempo y asistencia.",
        "unlock_sincerely": "Atentamente,",
    },
    "ht": {
        "lang_label": "🌐 Lang",
        "hero_subtitle": "📱 Aplikasyon Debloke Telefòn Ou",
        "hero_role": "Enjenyè Lojisyèl · Enjenyè-an-Chèf, GlobalInternet.py",
        "intro_title": "Byenveni nan Aplikasyon Debloke Telefòn Ou",
        "intro_text": "yon asistan pwofesyonèl tout-an-yon pou dyagnostik lejitim telefòn ak demann deblokaj operatè.",
        "intro_helps": "Zouti sa a ede w :",
        "intro_li1": "Validite nimewo IMEI nenpòt telefòn ak algoritm Luhn entènasyonal la",
        "intro_li2": "Chèche spesifikasyon aparèy pa mak ak modèl",
        "intro_li3": "Jenere demann ofisyèl deblokaj pou voye bay Digicel, Natcom, oswa nenpòt operatè",
        "intro_li4": "Jwenn konsiltasyon dirèk 1-a-1 ak Gesner pou depannaj avanse",
        "intro_warn": "⚠️ Enpòtan : Aplikasyon sa a sipòte sèlman operasyon lejitim. Nou PA kontourne ekran blokaj, FRP, iCloud, oswa nenpòt fonksyon sekirite. Tout sèvis mande prèv pwopriyete aparèy la.",
        "services_title": "🛠️ Sèvis Nou Yo",
        "svc1_title": "Validatè IMEI",
        "svc1_desc": "Tcheke si yon IMEI valid matematikman ak algoritm Luhn ofisyèl tout operatè mondyal yo itilize.",
        "svc2_title": "Chèche Aparèy",
        "svc2_desc": "Chèche spesifikasyon pa mak ak modèl. Jwenn enfòmasyon sou prosesè, depo, ak sistèm operasyon.",
        "svc3_title": "Deblokaj Operatè",
        "svc3_desc": "Jenere yon demann pwofesyonèl deblokaj pou voye bay operatè w (Digicel, Natcom, AT&T, elatriye).",
        "svc4_title": "Konsiltasyon",
        "svc4_desc": "Pale 1-a-1 ak Gesner sou WhatsApp pou depannaj avanse ak konsèy reparasyon.",
        "imei_title": "🔍 Validatè IMEI",
        "imei_input_label": "Antre nimewo IMEI 15 chif ou",
        "imei_input_placeholder": "eg. 358751234567890",
        "imei_help": "Konpoze *#06# sou telefòn ou pou wè IMEI w.",
        "imei_btn": "✅ Validye IMEI",
        "imei_len_err": "❌ IMEI dwe gen egzakteman 15 chif.",
        "imei_valid": "✅ IMEI Valid",
        "imei_valid_msg": "IMEI sa a pase som verifikasyon Luhn tout operatè itilize. Ou ka enkli l nan demann deblokaj ou anba a.",
        "imei_invalid": "❌ IMEI Envalid",
        "imei_invalid_msg": "IMEI sa a echwe som verifikasyon Luhn. Verifye nimewo a — konpoze *#06# pou wè bon IMEI a.",
        "device_title": "📋 Chèche Aparèy",
        "device_brand": "Mak",
        "device_model": "Modèl",
        "device_btn": "🔎 Chèche Aparèy",
        "device_not_found": "❌ Aparèy pa jwenn nan baz done nou. Kontakte Gesner pou yon rechèch pèsonalize.",
        "unlock_title": "🔓 Asistan Deblokaj Operatè",
        "unlock_intro": "Ranpli detay yo anba a. Aplikasyon an ap jenere yon imèl pwofesyonèl demann deblokaj ou ka voye dirèkteman bay operatè w (Digicel, Natcom, AT&T, T-Mobile, elatriye). Se sèl wout legal pou retire yon blokaj SIM.",
        "unlock_name": "Non Konplè Ou",
        "unlock_name_ph": "eg. Jan Batis",
        "unlock_email": "Adrès Imèl Ou",
        "unlock_email_ph": "ou@egzanp.com",
        "unlock_carrier": "Operatè Ou",
        "unlock_imei": "IMEI Aparèy (15 chif)",
        "unlock_imei_ph": "358751234567890",
        "unlock_device": "Modèl Aparèy",
        "unlock_device_ph": "eg. iPhone 12, Galaxy S21",
        "unlock_reason": "Rezon demann lan",
        "unlock_reason_ph": "Mwen se pwopriyetè orijinal la epi mwen vle itilize aparèy sa a ak yon lòt operatè.",
        "unlock_btn": "📧 Jenere Imèl Demann",
        "unlock_fill_all": "❌ Tanpri ranpli tout chan yo anvan w jenere imèl la.",
        "unlock_bad_imei": "❌ IMEI ou antre a pa valid. Verifye l epi eseye ankò.",
        "unlock_ready": "✅ Imèl demann ou pare. Kopye l anba a epi voye l bay operatè w.",
        "consult_title": "💬 Konsiltasyon Pèsonèl ak Gesner",
        "consult_intro": "Bezwen èd dirèk 1-a-1 pou yon pwoblèm telefòn? Rezève yon konsiltasyon pèsonèl ak Gesner. Li pral gide w sou WhatsApp — etap pa etap, an Kreyòl oswa Anglè.",
        "consult_includes": "Konsiltasyon an gen ladan :",
        "consult_li1": "Dyagnostik pèsonalize pwoblèm ou",
        "consult_li2": "Gid detaye pou solisyon lejitim",
        "consult_li3": "Konsèy deblokaj espesifik pou aparèy ou",
        "consult_li4": "Sipò swivi pandan 7 jou",
        "moncash_label": "💳 Peman MonCash",
        "moncash_amount": "Voye $5 USD · ~700 HTG",
        "moncash_note": "Louvri MonCash → Transfè → Prisme → Prisme. Antre nimewo ki anwo a → Konfime $5 → Kopye referans tranzaksyon ou",
        "consult_name": "Non Ou",
        "consult_name_ph": "Non konplè",
        "consult_phone": "Nimewo WhatsApp Ou",
        "consult_phone_ph": "+509 XXXX XXXX",
        "consult_ref": "Referans Tranzaksyon MonCash",
        "consult_ref_ph": "eg. MC987654321",
        "consult_issue": "Pwoblèm Ou (kout)",
        "consult_issue_ph": "eg. Pa ka debloke operatè",
        "consult_notes": "Di Gesner plis sou pwoblèm ou",
        "consult_notes_ph": "Dekri sa ou bezwen èd pou li…",
        "consult_btn": "📩 Soumèt Demann Konsiltasyon",
        "consult_fill": "❌ Tanpri ranpli non w, nimewo WhatsApp, ak referans MonCash.",
        "consult_thanks": "✅ Mèsi,",
        "consult_received": "Demann konsiltasyon ou resevwa.",
        "consult_contact": "Gesner ap kontakte w sou WhatsApp nan 24 èdtan nan",
        "consult_ref_label": "Referans MonCash ou :",
        "consult_urgent": "Pou ijans, rele",
        "consult_directly": "dirèkteman.",
        "safety_title": "🛡️ Konfyans ak Sekirite",
        "safety_notdo": "⚠️ Sa aplikasyon sa a PA fè :",
        "safety_not1": "PA kontourne ekran blokaj (PIN, modèl, modpas)",
        "safety_not2": "PA kontourne blokaj aktivasyon iCloud",
        "safety_not3": "PA kontourne FRP Google",
        "safety_not4": "PA kontourne okenn fonksyon sekirite manifakti oswa pwopriyetè",
        "safety_do": "✅ Sa aplikasyon sa a FÈ :",
        "safety_do1": "Validye nimewo IMEI (algoritm Luhn)",
        "safety_do2": "Chèche spesifikasyon lejitim aparèy",
        "safety_do3": "Jenere imèl demann deblokaj operatè",
        "safety_do4": "Konekte w ak yon teknisyen sètifye pou konsiltasyon",
        "safety_protection": "Pou pwoteksyon w : Nou mande prèv pwopriyete pou tout sèvis. Nenpòt tantativ pou kontourne sekirite sou yon aparèy ou pa posede entèdi e ka ilegal.",
        "footer_role": "Enjenyè Lojisyèl · Enjenyè-an-Chèf, GlobalInternet.py",
        "footer_built": "© 2026 Aplikasyon Debloke Telefòn Ou · Bati ak Streamlit",
        "unlock_subject": "Sijè : Demann Deblokaj Operatè — IMEI",
        "unlock_dear": "Chè",
        "unlock_support": "Sèvis Kliyan,",
        "unlock_body1": "Mwen ekri pou mande fòmèlman yon deblokaj rezo SIM pou aparèy mwen. Mwen se pwopriyetè orijinal la epi mwen ranpli tout obligasyon kontra mwen.",
        "unlock_body2": "Tanpri jwenn detay yo anba a :",
        "unlock_owner_name": "Non Pwopriyetè :",
        "unlock_owner_email": "Imèl Pwopriyetè :",
        "unlock_device_model": "Modèl Aparèy :",
        "unlock_imei_label": "IMEI :",
        "unlock_carrier_label": "Operatè :",
        "unlock_reason_label": "Rezon demann lan :",
        "unlock_reason_default": "Mwen vle itilize aparèy sa a ak yon lòt rezo.",
        "unlock_attached": "Mwen tache prèv acha m ak yon kopi ID m pou verifikasyon. Tanpri trete demann sa a pi vit posib.",
        "unlock_thanks": "Mèsi pou tan w ak asistans ou.",
        "unlock_sincerely": "Senchèman,",
    },
}

# =========================================================
# LANGUAGE SELECTOR
# =========================================================
LANG_OPTIONS = {
    "English": "en",
    "Français": "fr",
    "Español": "es",
    "Kreyòl Ayisyen": "ht",
}

if "lang" not in st.session_state:
    st.session_state.lang = "en"

# Top-of-page language selector (3-column layout for centering)
_lc1, _lc2, _lc3 = st.columns([1, 2, 1])
with _lc2:
    selected_lang_name = st.selectbox(
        T[st.session_state.lang]["lang_label"],
        options=list(LANG_OPTIONS.keys()),
        index=list(LANG_OPTIONS.values()).index(st.session_state.lang),
        key="lang_selector",
    )
    new_lang = LANG_OPTIONS[selected_lang_name]
    if new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
        st.rerun()

# Shortcut to current translation dictionary
t = T[st.session_state.lang]

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
    html, body, .stApp {
        background: linear-gradient(160deg, #4A9EE0 0%, #3A87CC 45%, #2E7BC4 100%) !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
    }
    .main, .block-container, section.main {
        background: transparent !important;
        color: #ffffff !important;
    }
    h1, h2, h3, h4, h5, h6, p, span, div, label, li, ul, ol {
        color: #ffffff;
    }

    /* --- Hero --- */
    .hero-header {
        background: linear-gradient(180deg, rgba(255,255,255,.18), rgba(255,255,255,.10));
        border: 3px solid #ffffff;
        border-radius: 22px;
        padding: 28px 24px;
        text-align: center;
        margin-bottom: 24px;
        box-shadow: 0 16px 50px rgba(0,0,0,.30), 0 0 60px rgba(255,255,255,.35);
        backdrop-filter: blur(6px);
    }
    .hero-title {
        font-size: clamp(2rem, 5vw, 3.4rem);
        font-weight: 900;
        letter-spacing: 4px;
        line-height: 1.05;
        color: #ffffff !important;
        text-shadow: 0 3px 18px rgba(0,0,0,.35), 0 0 40px rgba(255,255,255,.45);
        margin: 0;
    }
    .hero-subtitle {
        font-size: clamp(1rem, 2vw, 1.4rem);
        font-weight: 800;
        letter-spacing: 4px;
        color: #ffffff !important;
        text-transform: uppercase;
        margin: 8px 0 6px;
        text-shadow: 0 2px 12px rgba(0,0,0,.30);
    }
    .hero-role {
        font-size: clamp(.72rem, 1.2vw, .88rem);
        font-weight: 700;
        letter-spacing: 3px;
        color: #ffffff !important;
        text-transform: uppercase;
        margin-bottom: 16px;
        opacity: .92;
    }
    .hero-contact {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 12px;
        font-size: clamp(.88rem, 1.4vw, 1.05rem);
        font-weight: 800;
    }
    .hero-contact span {
        display: inline-flex;align-items:center;gap:6px;
        padding: 8px 16px;border-radius:999px;
        background: rgba(255,255,255,.22);
        border: 1px solid rgba(255,255,255,.55);
        color: #ffffff !important;
        backdrop-filter: blur(4px);
    }
    .hero-contact a {
        color: #ffffff !important;
        text-decoration: none;
        font-weight: 900;
        border-bottom: 1px dotted rgba(255,255,255,.7);
    }
    .hero-contact a:hover { color: #FFF9C4 !important; }

    /* --- Feature cards --- */
    .feature-card {
        background: rgba(255,255,255,.16);
        border: 2px solid rgba(255,255,255,.55);
        border-radius: 18px;
        padding: 20px;
        height: 100%;
        box-shadow: 0 10px 30px rgba(0,0,0,.20);
        transition: all .25s ease;
        backdrop-filter: blur(6px);
    }
    .feature-card:hover {
        border-color: #ffffff;
        transform: translateY(-4px);
        box-shadow: 0 14px 40px rgba(0,0,0,.30), 0 0 40px rgba(255,255,255,.45);
        background: rgba(255,255,255,.24);
    }
    .feature-icon { font-size:2.2rem;line-height:1;margin-bottom:10px;filter:drop-shadow(0 0 12px rgba(255,255,255,.8)); }
    .feature-title { font-size:1.05rem;font-weight:900;letter-spacing:1px;color:#ffffff !important;margin-bottom:6px; }
    .feature-desc { font-size:.85rem;color:#ffffff !important;line-height:1.55;font-weight:600;opacity:.95; }

    /* --- MonCash --- */
    .moncash-box {
        background: linear-gradient(135deg, rgba(255,255,255,.24), rgba(255,255,255,.14));
        border: 3px solid #ffffff;
        border-radius: 20px;
        padding: 22px;
        text-align: center;
        margin: 16px 0 20px;
        box-shadow: 0 0 40px rgba(255,255,255,.35);
        backdrop-filter: blur(6px);
    }
    .moncash-label { font-size:.78rem;letter-spacing:3px;color:#ffffff !important;text-transform:uppercase;font-weight:900;margin-bottom:8px; }
    .moncash-number {
        font-size: clamp(1.6rem, 4vw, 2.4rem);
        font-weight: 900;
        font-family: 'Courier New', monospace;
        color: #FFEB3B !important;
        text-shadow: 0 3px 20px rgba(0,0,0,.35), 0 0 30px rgba(255,235,59,.75);
        letter-spacing: 3px;margin: 6px 0;
    }
    .moncash-amount { font-size:1.1rem;font-weight:900;color:#00E676 !important;letter-spacing:1.5px;text-shadow:0 2px 12px rgba(0,0,0,.30); }
    .moncash-note { font-size:.78rem;color:#ffffff !important;font-weight:700;margin-top:8px;letter-spacing:.5px;opacity:.95; }

    /* --- Section title --- */
    .section-title {
        font-size: clamp(1.3rem, 2.6vw, 1.8rem);
        font-weight: 900;letter-spacing:2px;
        color: #FFEB3B !important;
        margin: 20px 0 10px;
        text-shadow: 0 2px 14px rgba(0,0,0,.35), 0 0 20px rgba(255,235,59,.4);
    }

    /* --- Result boxes --- */
    .result-good {
        background: rgba(0,255,136,.22);
        border: 2px solid #ffffff;
        border-radius: 14px;padding: 16px;
        color: #00E676 !important;
        font-weight: 800;font-size: 1rem;
        text-shadow: 0 1px 4px rgba(0,0,0,.35);
        backdrop-filter: blur(4px);
    }
    .result-good b { color:#ffffff !important; }
    .result-bad {
        background: rgba(255,59,59,.22);
        border: 2px solid #ffffff;
        border-radius: 14px;padding: 16px;
        color: #FF8A80 !important;
        font-weight: 800;font-size: 1rem;
        text-shadow: 0 1px 4px rgba(0,0,0,.35);
        backdrop-filter: blur(4px);
    }
    .result-bad b { color:#ffffff !important; }

    .intro-box {
        max-width: 900px;margin: 0 auto 24px;
        padding: 18px 22px;border-radius: 16px;
        background: rgba(255,255,255,.16);
        border: 1px solid rgba(255,255,255,.45);
        color: #ffffff !important;
        font-size: 1rem;line-height: 1.65;font-weight: 600;
        backdrop-filter: blur(6px);
    }
    .safety-box {
        background: rgba(255,255,255,.16);
        border: 2px solid #ffffff;border-radius: 16px;
        padding: 20px 22px;
        color: #ffffff !important;
        line-height: 1.65;font-weight: 600;font-size: .92rem;
        backdrop-filter: blur(6px);
    }

    /* --- Inputs (bright gold / cyan on focus) --- */
    .stTextInput input {
        background: rgba(255,255,255,.22) !important;
        color: #FFEB3B !important;
        border: 2px solid rgba(255,255,255,.55) !important;
        border-radius: 10px !important;
        font-weight: 900 !important;font-size: 1rem !important;
        letter-spacing: .5px !important;
        text-shadow: 0 1px 3px rgba(0,0,0,.35) !important;
        transition: all .2s ease !important;
    }
    .stTextInput input::placeholder { color: rgba(255,255,255,.55) !important;font-weight:700 !important;font-style:italic !important; }
    .stTextInput input:focus {
        background: rgba(255,255,255,.32) !important;
        color: #00E5FF !important;
        border: 2px solid #00E5FF !important;
        box-shadow: 0 0 0 3px rgba(0,229,255,.35), 0 0 24px rgba(0,229,255,.55) !important;
        text-shadow: 0 0 12px rgba(0,229,255,.7) !important;
    }
    .stTextArea textarea {
        background: rgba(255,255,255,.22) !important;
        color: #FFEB3B !important;
        border: 2px solid rgba(255,255,255,.55) !important;
        border-radius: 10px !important;
        font-weight: 800 !important;font-size: .96rem !important;
        letter-spacing: .3px !important;
        text-shadow: 0 1px 3px rgba(0,0,0,.35) !important;
        transition: all .2s ease !important;
    }
    .stTextArea textarea::placeholder { color: rgba(255,255,255,.55) !important;font-weight:700 !important;font-style:italic !important; }
    .stTextArea textarea:focus {
        background: rgba(255,255,255,.32) !important;
        color: #00E5FF !important;
        border: 2px solid #00E5FF !important;
        box-shadow: 0 0 0 3px rgba(0,229,255,.35), 0 0 24px rgba(0,229,255,.55) !important;
        text-shadow: 0 0 12px rgba(0,229,255,.7) !important;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        background: rgba(255,255,255,.22) !important;
        border: 2px solid rgba(255,255,255,.55) !important;
        border-radius: 10px !important;
        transition: all .2s ease !important;
    }
    .stSelectbox div[data-baseweb="select"] div,
    .stSelectbox div[data-baseweb="select"] span,
    .stSelectbox div[data-baseweb="select"] input,
    .stSelectbox div[data-baseweb="select"] [class*="ValueContainer"],
    .stSelectbox div[data-baseweb="select"] [class*="singleValue"] {
        color: #FFEB3B !important;
        font-weight: 900 !important;
        letter-spacing: .5px !important;
        text-shadow: 0 1px 3px rgba(0,0,0,.35) !important;
    }
    .stSelectbox div[data-baseweb="select"]:focus-within > div {
        background: rgba(255,255,255,.32) !important;
        border: 2px solid #00E5FF !important;
        box-shadow: 0 0 0 3px rgba(0,229,255,.35), 0 0 24px rgba(0,229,255,.55) !important;
    }
    .stSelectbox div[data-baseweb="select"]:focus-within span,
    .stSelectbox div[data-baseweb="select"]:focus-within [class*="singleValue"] {
        color: #00E5FF !important;
        text-shadow: 0 0 12px rgba(0,229,255,.8) !important;
    }
    .stSelectbox div[data-baseweb="select"] svg {
        fill: #ffffff !important;
        color: #ffffff !important;
    }
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] li,
    div[role="listbox"] { background: #2E7BC4 !important;color:#ffffff !important;border-radius:10px !important; }
    div[role="option"] { color: #FFEB3B !important;font-weight:800 !important;background: #2E7BC4 !important; }
    div[role="option"]:hover { background: rgba(0,229,255,.35) !important;color:#00E5FF !important; }
    div[role="option"][aria-selected="true"] { background: rgba(255,235,59,.30) !important;color:#FFEB3B !important;font-weight:900 !important; }

    .stTextInput label,
    .stTextArea label,
    .stSelectbox label {
        color: #ffffff !important;
        font-weight: 800 !important;
        letter-spacing: .5px !important;
        text-shadow: 0 1px 3px rgba(0,0,0,.30) !important;
    }

    /* --- Buttons --- */
    .stButton > button {
        background: #ffffff !important;
        color: #2E7BC4 !important;
        font-weight: 900 !important;
        border-radius: 12px !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 4px 0 rgba(0,0,0,.20) !important;
        transition: all .12s !important;
        letter-spacing: 1px !important;
    }
    .stButton > button:hover { background: #FFEB3B !important;color:#1A3A5C !important;transform:translateY(-1px); }
    .stButton > button:active { transform:translateY(3px) !important;box-shadow:0 1px 0 rgba(0,0,0,.20) !important; }
    div[data-testid="stFormSubmitButton"] button {
        background: #FFEB3B !important;color:#1A3A5C !important;
        font-weight: 900 !important;border: 2px solid #ffffff !important;
    }
    div[data-testid="stFormSubmitButton"] button:hover { background: #00E5FF !important;color:#1A3A5C !important; }

    /* --- Code block --- */
    .stCodeBlock, pre, code {
        background: rgba(0,0,0,.32) !important;
        color: #00E5FF !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,.35) !important;
    }
    pre code, code span { color:#00E5FF !important;font-weight:700 !important; }
    .stMarkdown, .stMarkdown * { color: #ffffff !important; }
    .stTooltipIcon svg { fill: #FFEB3B !important;color:#FFEB3B !important; }

    /* --- Footer --- */
    .app-footer {
        text-align: center;
        padding: 24px 16px 12px;
        border-top: 2px solid rgba(255,255,255,.35);
        margin-top: 30px;
        color: #ffffff !important;
        font-size: .78rem;font-weight: 700;letter-spacing: .6px;
    }
    .app-footer .fname {
        font-size: 1rem;font-weight:900;color:#FFEB3B !important;
        letter-spacing: 2px;margin-bottom: 4px;
        text-shadow: 0 2px 14px rgba(0,0,0,.35), 0 0 22px rgba(255,235,59,.5);
    }
    .app-footer .frole {
        font-size: .7rem;letter-spacing:2px;text-transform:uppercase;
        color: #ffffff !important;margin-bottom: 8px;opacity: .92;
    }
    .app-footer a {
        color: #00E5FF !important;text-decoration:none;font-weight:800;
        margin: 0 6px;border-bottom: 1px dotted rgba(0,229,255,.7);
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO HEADER
# =========================================================
st.markdown(f"""
<div class="hero-header">
    <h1 class="hero-title">GESNER DESLANDES</h1>
    <div class="hero-subtitle">{t['hero_subtitle']}</div>
    <div class="hero-role">{t['hero_role']}</div>
    <div class="hero-contact">
        <span>📞 <a href="tel:+50947385663">(509) 4738-5663</a></span>
        <span>✉️ <a href="mailto:deslandes78@gmail.com">deslandes78@gmail.com</a></span>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# INTRODUCTION
# =========================================================
st.markdown(f"""
<div class="intro-box">
    <b>{t['intro_title']}</b> — {t['intro_text']}<br><br>
    {t['intro_helps']}
    <ul style="margin: 8px 0 0 20px; padding: 0;">
        <li>✅ {t['intro_li1']}</li>
        <li>✅ {t['intro_li2']}</li>
        <li>✅ {t['intro_li3']}</li>
        <li>✅ {t['intro_li4']}</li>
    </ul>
    <br>
    <b>{t['intro_warn']}</b>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SERVICES
# =========================================================
st.markdown(f'<div class="section-title">{t["services_title"]}</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">{t['svc1_title']}</div>
        <div class="feature-desc">{t['svc1_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">📋</div>
        <div class="feature-title">{t['svc2_title']}</div>
        <div class="feature-desc">{t['svc2_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">🔓</div>
        <div class="feature-title">{t['svc3_title']}</div>
        <div class="feature-desc">{t['svc3_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">💬</div>
        <div class="feature-title">{t['svc4_title']}</div>
        <div class="feature-desc">{t['svc4_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# SECTION 1 — IMEI VALIDATOR
# =========================================================
st.markdown(f'<div class="section-title">{t["imei_title"]}</div>', unsafe_allow_html=True)

def luhn_check(imei: str) -> bool:
    if not imei.isdigit() or len(imei) != 15:
        return False
    total = 0
    for i, ch in enumerate(imei):
        d = int(ch)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

imei_input = st.text_input(
    t["imei_input_label"],
    max_chars=15,
    placeholder=t["imei_input_placeholder"],
    help=t["imei_help"],
    key="imei_input_widget",
)

col_a, col_b = st.columns([1, 3])
with col_a:
    check_imei = st.button(t["imei_btn"], use_container_width=True, key="imei_check_btn")

if check_imei:
    imei_clean = re.sub(r"\D", "", imei_input or "")
    if len(imei_clean) != 15:
        st.markdown(f'<div class="result-bad">{t["imei_len_err"]}</div>', unsafe_allow_html=True)
    elif luhn_check(imei_clean):
        st.markdown(f"""
        <div class="result-good">
            {t['imei_valid']} — <b>{imei_clean}</b><br>
            {t['imei_valid_msg']}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-bad">
            {t['imei_invalid']} — <b>{imei_clean}</b><br>
            {t['imei_invalid_msg']}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SECTION 2 — DEVICE LOOKUP
# =========================================================
st.markdown(f'<div class="section-title">{t["device_title"]}</div>', unsafe_allow_html=True)

DEVICE_DB = {
    ("Apple", "iPhone 12"): "A14 Bionic · 6.1\" OLED · 64/128/256 GB · iOS 14+",
    ("Apple", "iPhone 13"): "A15 Bionic · 6.1\" OLED · 128/256/512 GB · iOS 15+",
    ("Apple", "iPhone 14"): "A15 Bionic · 6.1\" OLED · 128/256/512 GB · iOS 16+",
    ("Samsung", "Galaxy S21"): "Exynos 2100 · 6.2\" AMOLED · 128/256 GB · Android 11+",
    ("Samsung", "Galaxy S22"): "Snapdragon 8 Gen 1 · 6.1\" AMOLED · 128/256 GB · Android 12+",
    ("Samsung", "Galaxy A54"): "Exynos 1380 · 6.4\" AMOLED · 128/256 GB · Android 13+",
    ("Xiaomi", "Redmi Note 12"): "Snapdragon 685 · 6.67\" AMOLED · 64/128/256 GB · Android 13",
    ("Xiaomi", "Poco X5"): "Snapdragon 695 · 6.67\" AMOLED · 128/256 GB · Android 13",
    ("Tecno", "Spark 10"): "Helio G37 · 6.6\" IPS · 64/128 GB · Android 13",
    ("Tecno", "Camon 20"): "Helio G85 · 6.67\" AMOLED · 128/256 GB · Android 13",
    ("Infinix", "Hot 30"): "Helio G88 · 6.78\" IPS · 128/256 GB · Android 13",
    ("Itel", "A60"): "Unisoc SC9863A · 6.6\" IPS · 32/64 GB · Android 12",
}

col_x, col_y = st.columns(2)
with col_x:
    brand = st.selectbox(t["device_brand"], sorted(set(k[0] for k in DEVICE_DB)), key="brand_select")
with col_y:
    models = sorted([k[1] for k in DEVICE_DB if k[0] == brand])
    model = st.selectbox(t["device_model"], models, key="model_select")

if st.button(t["device_btn"], key="device_lookup_btn"):
    specs = DEVICE_DB.get((brand, model))
    if specs:
        st.markdown(f"""
        <div class="result-good">
            📱 <b>{brand} {model}</b><br>
            {specs}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="result-bad">{t["device_not_found"]}</div>', unsafe_allow_html=True)

# =========================================================
# SECTION 3 — CARRIER UNLOCK ASSISTANT
# =========================================================
st.markdown(f'<div class="section-title">{t["unlock_title"]}</div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="color:#ffffff; font-size:.92rem; font-weight:600; line-height:1.6; margin-bottom:14px;">
    {t['unlock_intro']}
</div>
""", unsafe_allow_html=True)

with st.form("unlock_form"):
    fcol1, fcol2 = st.columns(2)
    with fcol1:
        owner_name = st.text_input(t["unlock_name"], placeholder=t["unlock_name_ph"])
        owner_email = st.text_input(t["unlock_email"], placeholder=t["unlock_email_ph"])
    with fcol2:
        carrier = st.selectbox(t["unlock_carrier"], ["Digicel Haiti", "Natcom Haiti", "AT&T", "T-Mobile", "Verizon", "Other"])
        imei_unlock = st.text_input(t["unlock_imei"], max_chars=15, placeholder=t["unlock_imei_ph"])

    device_info = st.text_input(t["unlock_device"], placeholder=t["unlock_device_ph"])
    reason = st.text_area(t["unlock_reason"], placeholder=t["unlock_reason_ph"], height=80)

    submitted = st.form_submit_button(t["unlock_btn"], use_container_width=True)

if submitted:
    imei_clean = re.sub(r"\D", "", imei_unlock or "")
    if not owner_name or not owner_email or not imei_clean or not device_info:
        st.markdown(f'<div class="result-bad">{t["unlock_fill_all"]}</div>', unsafe_allow_html=True)
    elif len(imei_clean) != 15 or not luhn_check(imei_clean):
        st.markdown(f'<div class="result-bad">{t["unlock_bad_imei"]}</div>', unsafe_allow_html=True)
    else:
        email_body = f"""{t['unlock_subject']} {imei_clean}

{t['unlock_dear']} {carrier} {t['unlock_support']}

{t['unlock_body1']}

{t['unlock_body2']}

    {t['unlock_owner_name']}     {owner_name}
    {t['unlock_owner_email']}    {owner_email}
    {t['unlock_device_model']}   {device_info}
    {t['unlock_imei_label']}           {imei_clean}
    {t['unlock_carrier_label']}        {carrier}

{t['unlock_reason_label']}
    {reason if reason else t['unlock_reason_default']}

{t['unlock_attached']}

{t['unlock_thanks']}

{t['unlock_sincerely']}
{owner_name}
{owner_email}
"""
        st.markdown(f'<div class="result-good">{t["unlock_ready"]}</div>', unsafe_allow_html=True)
        st.code(email_body, language="text")

# =========================================================
# SECTION 4 — PAID CONSULTATION
# =========================================================
st.markdown(f'<div class="section-title">{t["consult_title"]}</div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="color:#ffffff; font-size:.95rem; font-weight:600; line-height:1.65; margin-bottom:16px;">
    {t['consult_intro']}<br><br>
    <b>{t['consult_includes']}</b><br>
    • {t['consult_li1']}<br>
    • {t['consult_li2']}<br>
    • {t['consult_li3']}<br>
    • {t['consult_li4']}
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="moncash-box">
    <div class="moncash-label">{t['moncash_label']}</div>
    <div class="moncash-number">(509) 4738-5663</div>
    <div class="moncash-amount">{t['moncash_amount']}</div>
    <div class="moncash-note">{t['moncash_note']}</div>
</div>
""", unsafe_allow_html=True)

with st.form("consult_form"):
    cc1, cc2 = st.columns(2)
    with cc1:
        client_name = st.text_input(t["consult_name"], placeholder=t["consult_name_ph"])
        client_phone = st.text_input(t["consult_phone"], placeholder=t["consult_phone_ph"])
    with cc2:
        moncash_ref = st.text_input(t["consult_ref"], placeholder=t["consult_ref_ph"])
        device_issue = st.text_input(t["consult_issue"], placeholder=t["consult_issue_ph"])

    consult_notes = st.text_area(t["consult_notes"], placeholder=t["consult_notes_ph"], height=90)

    consult_submit = st.form_submit_button(t["consult_btn"], use_container_width=True)

if consult_submit:
    if not client_name or not client_phone or not moncash_ref:
        st.markdown(f'<div class="result-bad">{t["consult_fill"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-good">
            {t['consult_thanks']} <b>{client_name}</b>!<br>
            {t['consult_received']}<br><br>
            📞 {t['consult_contact']} <b>{client_phone}</b>.<br>
            💳 {t['consult_ref_label']} <b>{moncash_ref}</b><br><br>
            {t['consult_urgent']} <b>(509) 4738-5663</b> {t['consult_directly']}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TRUST & SAFETY
# =========================================================
st.markdown(f'<div class="section-title">{t["safety_title"]}</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="safety-box">
    <b style="font-size:1.05rem;">{t['safety_notdo']}</b><br><br>
    • ❌ {t['safety_not1']}<br>
    • ❌ {t['safety_not2']}<br>
    • ❌ {t['safety_not3']}<br>
    • ❌ {t['safety_not4']}<br><br>
    <b style="font-size:1.05rem;">{t['safety_do']}</b><br><br>
    • ✅ {t['safety_do1']}<br>
    • ✅ {t['safety_do2']}<br>
    • ✅ {t['safety_do3']}<br>
    • ✅ {t['safety_do4']}<br><br>
    <b>{t['safety_protection']}</b>
</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown(f"""
<div class="app-footer">
    <div class="fname">GESNER DESLANDES</div>
    <div class="frole">{t['footer_role']}</div>
    <div>
        📞 <a href="tel:+50947385663">(509) 4738-5663</a> &nbsp;·&nbsp;
        ✉️ <a href="mailto:deslandes78@gmail.com">deslandes78@gmail.com</a>
    </div>
    <div style="margin-top: 12px; font-size: .68rem; opacity: .8;">
        {t['footer_built']}
    </div>
</div>
""", unsafe_allow_html=True)
