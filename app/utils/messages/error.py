
ERR_MSG = {
    "invalid_email": {
        "response_code": 400,
        "success": False,
        "message": {
            "ID": "Email dan pasword tidak valid",
            "EN": "Invalid email and password",
        },
         "data": {}
    },
    "email_not_found" : {
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Email tidak ditemukan",
            "EN" : "Email not found"
        },
    },
    "email_already_exist": {
        "response_code": 400,
        "success": False,
        "message": {
            "ID": "Email sudah terdaftar",
            "EN": "Email already exists",
        },
         "data": {}
    },
    "team_email_already_exist" :{
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Email sudah terdaftar di tim lain",
            "EN" : "Email already exists in another team"
        },
    },
    "email_not_verified": {
        "response_code": 401,
        "success": False,
        "message": {
            "ID": "Email belum diverifikasi",
            "EN": "Email not verified",
        },
         "data": {}
    },
    "email_already_verified": {
        "response_code": 400,
        "success": False,
        "message": {
            "ID": "Email sudah diverifikasi",
            "EN": "Email already verified",
        },
         "data": {}
    },  
    "invalid_auth": {
        "response_code": 400,
        "success": False,
        "message": {
            "ID": "Email atau pasword tidak valid",
            "EN": "Invalid email or password",
        },
        "data": {}
    },
    "invalid_old_password": {
        "response_code": 400,
        "success": False,
        "message": {
            "ID": "Password Lama tidak valid",
            "EN": "Invalid Old Password",
        },
    },
    "internal_server_error": {
        "response_code": 500,
        "success": False,
        "message": {
            "ID": "Terjadi kesalahan pada server",
            "EN": "Server error occurred",
        },
        "data": {}
    },
    "invalid_otp": {
            "response_code": 400,
            "success": False,
            "message": {
                "ID": "OTP tidak valid",
                "EN": "Invalid OTP",
            },
            "data": {}
        },
    "expired_otp": {
        "response_code": 400,
        "success": False,
        "message": {
            "ID": "OTP sudah kadaluarsa",
            "EN": "OTP has expired",
        },
        "data": {}
    },
    "used_otp": {
        "response_code": 400,
        "success": False,
        "message": {
            "ID": "OTP sudah digunakan",
            "EN": "OTP has been used",
        },
        "data": {}
    }, "invalid_token": {
        "response_code": 401,
        "success": False,
        "message": {
            "ID": "Token tidak valid",
            "EN": "Invalid token",
        },
        "data": {}
    },
    # Organization

    "customer_not_found": {
        "response_code": 404,
        "success": False,
        "message": {
            "ID": "Customer tidak ditemukan",
            "EN": "Customer not found",
        },
        "data": {}
    },

    "organisation_limit_exceeded": {
        "response_code": 400,
        "success": False,
        "message": {
            "ID": "Batas organisasi telah tercapai",
            "EN": "Organisation limit exceeded",
        },
        "data": {}
    },

    "quota_type_not_found" : {
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Tipe kuota tidak ditemukan",
            "EN" : "Quota type not found"
        },
        "data" : {}
    },

    "team_member_limit_exceeded" :{
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Batas anggota tim telah tercapai",
            "EN" : "Team member limit exceeded"
        },
    },
    "team_not_found" :{
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Tim tidak ditemukan",
            "EN" : "Team not found"
        },
    },

    "subscription_expired": {
        "response_code": 400,
        "success": False,
        "message": {
            "ID": "Langganan telah berakhir, silahhkan perpanjang langganan anda",
            "EN": "Subscription has expired, please renew your subscription",
        },
        "data": {}
    },

    "organisation_not_found": {
        "response_code": 404,
        "success": False,
        "message": {
            "ID": "Organisasi tidak ditemukan",
            "EN": "Organisation not found",
        },
        "data": {}
    },
    "organisation_id_required" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "ID Organisasi diperlukan",
            "EN" : "Organisation ID is required"
        },
        "data" : {}
    },

    "not_your_organisation": {
        "response_code": 401,
        "success": False,
        "message": {
            "ID": "Organisasi bukan milik Anda",
            "EN": "Organisation is not yours",
        },
        "data": {}
    },

    "organisation_already_exist" : {
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Nama Organisasi sudah ada silahkan ganti nama organisasi anda",
            "EN" : "The organization name already exists, please change your organization name"
        },
        "data" : {}
    },

    # Permission Denied
    "permission_denied": {
        "response_code": 403,
        "success": False,
        "message": {
            "ID": "Akses ditolak",
            "EN": "Permission denied",
        },
        "data": {}
    },
    
    # Admin
    "admin_not_found" : {
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Admin tidak ditemukan",
            "EN" : "Admin not found"
        },
        "data" : {}
    },
    "admin_invalid_password" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Password Admin tidak valid",
            "EN" : "Admin password is not valid"
        },
        "data" : {}
    },

    # plan 
    "plan_already_exist" :{
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Plan sudah ada",
            "EN" : "Plan already exist"
        },
        "data" : {}
    }, 
    "invalid_plan" : {
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Plan tidak valid",
            "EN" : "Invalid plan"
        },
        "data" : {}
    } ,
    "plan_not_found" : {
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Plan tidak ditemukan",
            "EN" : "Plan not found"
        },
        "data" : {}
    },

    # Documents
    "file_extension_not_allowed" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Ekstensi file tidak diizinkan. Hanya .jpg, .jpeg, .png, .pdf yang diizinkan",
            "EN" : "File extension not allowed. Only .jpg, .jpeg, .png, .pdf are allowed"
        },
        "data" : {}
    },
    "file_mime_type_not_allowed" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Tipe file tidak valid. Hanya gambar dan file PDF yang diizinkan",
            "EN" : "Invalid file type. Only images and PDF files are allowed"
        },
        "data" : {}
    },
    "document_not_found" : {
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Dokumen tidak ditemukan",
            "EN" : "Document not found"
        },
        "data" : {}
    } ,
    "not_your_doc" : {
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Dokumen bukan milik Anda",
            "EN" : "Document is not yours"
        },
        "data" : {}
    },
    "doc_already_extracted":{
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Dokumen sudah diekstrak",
            "EN" : "Document already extracted"
        },
        "data" : {}
    },


    "source_not_created" :{
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Sumber tidak dibuat",
            "EN" : "Source not created"
        },
        "data" : {}
    }, 
    "source_already_exist" :{
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Sumber sudah ada",
            "EN" : "Source already exist"
        },
        "data" : {}
    },
    "text_extraction_quota_exceeded" :{
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Kuota ekstraksi teks telah habis",
            "EN" : "Text extraction quota exceeded"
        },
        "data" : {}
    },
    "quota_exceeded" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Kuota telah habis",
            "EN" : "Quota has been exhausted"
        },
        "data" : {}
    },

    # datasets
    "model_not_found" :{
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Model tidak ditemukan",
            "EN" : "Model not found"
        },
        "data" : {}
    },
    "dataset_not_found" :{
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Dataset tidak ditemukan",
            "EN" : "Dataset not found"
        },
        "data" : {}
    },

    "source_extraction_not_found" :{
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Ekstraksi sumber tidak ditemukan",
            "EN" : "Source extraction not found"
        },
        "data" : {}
    },

    "quota_not_found" : {
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Anda belum memiliki kuota",
            "EN" : "You don't have a quota yet"
        },
        "data" : {}
    },


    # Session Not Found
    "session_not_found" :{
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Sesi tidak ditemukan",
            "EN" : "Session not found"
        },
        "data" : {}
    },

    "system_persona_not_deleted" :{
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Persona sistem tidak dihapus",
            "EN" : "System persona not deleted"
        },
        "data" : {}
    },
    "persona_not_found" :{
        "response_code" : 404,
        "success" : False,
        "message" : {
            "ID" : "Persona tidak ditemukan",
            "EN" : "Persona not found"
        },
        "data" : {}
    },
    "persona_limit_exceeded" :{
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Batas persona telah tercapai",
            "EN" : "Persona limit exceeded"
        },
        "data" : {}
    },


    "invalid_response_chat" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Maaf, Saya tidak mengerti permintaan Anda. Silahkan coba lagi.",
            "EN" : "Sorry, I couldn't process your request. Please try again."
        },
        "data" : {}
    },
    "invalid_response" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Respon tidak valid",
            "EN" : "Invalid response"
        },
        "data" : {}
    },

    "invalid_x_bypass_register" :{
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "X-Bypass-Register tidak valid",
            "EN" : "X-Bypass-Register is not valid"
        },
        "data" : {}
    }

    ,

    "message_limit_reached" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Batas pesan telah tercapai",
            "EN" : "Message limit reached"
        },
        "data" : {}
    },
    "LLM response is empty or invalid" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Respon LLM kosong atau tidak valid",
            "EN" : "LLM response is empty or invalid"
        },
        "data" : {}
    },
    "Invalid type" : {
        "response_code" : 400,
        "success" : False,
        "message" : {
            "ID" : "Tipe tidak valid",
            "EN" : "Invalid type"
        },
        "data" : {}
    }
}

