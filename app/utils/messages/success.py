from enum import Enum

SUCCESS_MESSAGES = {

    # Auth

    "login_successful": {
        "ID": "Login berhasil",
        "EN": "Login successful",
    }, 
    "register_successful": {
        "ID": "Registrasi berhasil",
        "EN": "Registration successful",
    },
    "verify_otp_successful": {
        "ID": "OTP berhasil diverifikasi",
        "EN": "OTP verified successfully",
    },
    "refresh_otp_successful": {
        "ID": "OTP baru telah dikirim ke email Anda",
        "EN": "New OTP has been sent to your email",
    }, 
    "get_customer_successful": {
        "ID": "Data customer berhasil ditemukan",
        "EN": "Customer data retrieved successfully",
    },
    "change_password_successful": {
        "ID": "Password berhasil diubah",
        "EN": "Password changed successfully",
    }, "forgot_password_successful": {
        "ID": "Token reset password berhasil dikirim",
        "EN": "Reset password token sent successfully"
    }, "reset_password_successful": {
        "ID": "Password berhasil direset",
        "EN": "Password reset successfully"
    }, "me_retrieved": {
        "ID": "Data user berhasil",
        "EN": "User data retrieved successfully"
    },

    # Organisation

    "organisation_created": {
        "ID": "Organisasi berhasil dibuat",
        "EN": "Organisation created successfully",
    },
    "organisation_updated": {
        "ID": "Organisasi berhasil diperbarui",
        "EN": "Organisation updated successfully",
    },
    "organisation_deleted": {
        "ID": "Organisasi berhasil dihapus",
        "EN": "Organisation deleted successfully",
    },
    "organisation_get": {
        "ID": "Data organisasi berhasil ditemukan",
        "EN": "Organisation data retrieved successfully",
    },
    "organisation_list": {
        "ID": "Data organisasi berhasil ditemukan",
        "EN": "Organisation data retrieved successfully",
    },
    "organisation_member_get" :{
        "ID": "Data anggota organisasi berhasil ditemukan",
        "EN": "Organisation member data retrieved successfully",
    },

    # ADMIN

    "admin_created": {
        "ID": "Admin berhasil dibuat",
        "EN": "Admin created successfully",
    },
    "admin_retrieved": {
        "ID": "Data admin berhasil ditemukan",
        "EN": "Admin data retrieved successfully",
    },
    "admin_updated":{
        "ID": "Admin berhasil diperbarui",
        "EN": "Admin updated successfully",
    },
     "admin_deactivated" :{
        "ID": "Admin berhasil dinonaktifkan",
        "EN": "Admin deactivated successfully",
     }, "customer_created" :{
        "ID": "Customer berhasil dibuat",
        "EN": "Customer created successfully",
     },

    #  Plan
    "plan_created" : {
        "ID": "Plan berhasil dibuat",
        "EN": "Plan created successfully",
    },
    "plan_retrieved" : {
        "ID": "Data plan berhasil ditemukan",
        "EN": "Plan data retrieved successfully",
    },
    "plan_deleted" : {
        "ID": "Plan berhasil dihapus",
        "EN": "Plan deleted successfully",
    },
    "plan_updated" :{
        "ID": "Plan berhasil diperbarui",
        "EN": "Plan updated successfully",
    },

    # Document
    "document_uploaded" : {
        "ID": "Dokumen berhasil diunggah",
        "EN": "Document uploaded successfully",
    },
    "document_retrieved" :{
        "ID": "Data dokumen berhasil ditemukan",
        "EN": "Document data retrieved successfully",
    },
    "document_deleted":{
        "ID": "Dokumen berhasil dihapus",
        "EN": "Document deleted successfully",
    },
    "document_extracted" :{
        "ID": "Data berhasil diekstrak",
        "EN": "Data extracted successfully",
    },
    "document_already_extracted" :{
        "ID": "Data sudah diekstrak",
        "EN": "Data already extracted",
    },
    "document_updated" :{
        "ID": "Dokumen berhasil diperbarui",
        "EN": "Document updated successfully",
    },
    "document_insight" :{
        "ID": "Insight berhasil ditemukan",
        "EN": "Insight data retrieved",
    },
    # "document_insight" :{
    #     "ID": "Insight berhasil ditemukan",
    #     "EN": "Insight data retrieved
    # },

    # Transaction
    "transaction_created":{
        "ID": "Transaksi berhasil dibuat",
        "EN": "Transaction created successfully",
    },
    "transaction_retrieved" :{
        "ID": "Data transaksi berhasil ditemukan",
        "EN": "Transaction data retrieved successfully",
    },


    # Source
    "source_uploaded" :{
        "ID": "Source berhasil diunggah",
        "EN": "Source uploaded successfully",
    },
    "quotas_retrieved" :{
        "ID": "Kuota berhasil diambil", 
        "EN": "Quota retrieved successfully",
    },
    "source_retrieved" : {
        "ID": "Data source berhasil ditemukan",
        "EN": "Source data retrieved successfully",
    },
    "source_deleted" : {
        "ID": "Source berhasil dihapus",
        "EN": "Source deleted successfully",
    },

    # teams member
    "team_member_invited" :{
        "ID": "Anggota tim berhasil diundang",
        "EN": "Team member invited successfully",
    },
    "team_member_deleted" :{
        "ID": "Anggota tim berhasil dihapus",
        "EN": "Team member deleted successfully",
    },
    "team_deleted" :{
        "ID": "Tim berhasil dihapus",
        "EN": "Team deleted successfully",
    },

    # datasets
    "dataset_created" :{
        "ID": "Dataset berhasil dibuat",
        "EN": "Dataset created successfully",
    },
    "dataset_retrieved" :{
        "ID": "Data dataset berhasil ditemukan",
        "EN": "Dataset data retrieved successfully",
    },
    "dataset_deleted" :{
        "ID": "Dataset berhasil dihapus",
        "EN": "Dataset deleted successfully",
    },

    # Saved Promps
    "saved_prompts_retrieved" :{
        "ID": "Prompts tersimpan berhasil ditemukan",
        "EN": "Saved prompts retrieved successfully",
    },
    "saved_prompt_created" : {
        "ID": "Prompts tersimpan berhasil dibuat",
        "EN": "Saved prompts created successfully",
    },


    "generate_rag" :{
        "ID": "Data berhasil dihasilkan",
        "EN": "Data generated successfully",
    },
    "report_downloaded" : {
        "ID": "Laporan berhasil diunduh",
        "EN": "Report downloaded successfully",
    },
    "reports_retrieved" :{
        "ID": "Data laporan berhasil ditemukan",
        "EN": "Report data retrieved successfully",
    }



    ,"update_onboarding_successful" :{
        "ID": "Onboarding berhasil diperbarui",
        "EN": "Onboarding updated successfully",
    },

    "update_profile_successful" :{
        "ID": "Profil berhasil diperbarui",
        "EN": "Profile updated successfully",
    }



    ,"session_created" :{
        "ID": "Sesi berhasil dibuat",
        "EN": "Session created successfully",
    },
    "retrieved_chat_history" : {
        "ID": "Histori chat berhasil ditemukan",
        "EN": "Chat history retrieved successfully",
    },
    "retrieved_sessions" : {
        "ID": "Sesi berhasil ditemukan",
        "EN": "Session retrieved successfully",
    }

    ,"retrieved_session" : {
        "ID": "Sesi berhasil ditemukan",
        "EN": "Session retrieved successfully",
    },"update_session_title" :{
        "ID": "Judul sesi berhasil diperbarui",
        "EN": "Session title updated successfully",
    },
    "session_deleted" :{
        "ID": "Sesi berhasil dihapus",
        "EN": "Session deleted successfully",
    },

    "quota_retrieved" :{
        "ID": "Kuota berhasil diambil",
        "EN": "Quota retrieved successfully",
    },

    "get_payment_methods" :{
        "ID": "Metode pembayaran berhasil ditemukan",
        "EN": "Payment methods retrieved successfully",
    },

    "persona_created" : {
        "ID": "Persona berhasil dibuat",
        "EN": "Persona created successfully",
    },
    "persona_retrieved" : {
        "ID": "Data persona berhasil ditemukan",
        "EN": "Persona data retrieved successfully",
    },
    "persona_updated" :{
        "ID": "Persona berhasil diperbarui",
        "EN": "Persona updated successfully",
    },
    "persona_deleted" :{
        "ID": "Persona berhasil dihapus",
        "EN": "Persona deleted successfully",
    },"chat_history_pdf_generated" :{
        "ID": "PDF histori chat berhasil dihasilkan",
        "EN": "Chat history PDF generated successfully",
    }


    # affiliate
    ,"affiliate_created" : {
        "ID": "Affiliate berhasil dibuat",
        "EN": "Affiliate created successfully",
    }

    # ============================== Legal Pulse ==================================
    ,"register_identities" : {
        "ID": "Identity berhasil dibuat",
        "EN": "Identity created successfully",
    }
}


class SuccessMessages(Enum):
    RegisterIdentities = {
        "ID": "Identity berhasil dibuat",
        "EN": "Identity created successfully",
    }

    SendMessage = {
        "ID": "Pesan berhasil dikirim",
        "EN": "Message sent successfully",
    }

    AnalyticEducation = {
        "ID": "Data edukasi berhasil ditemukan",
        "EN": "Education data retrieved successfully",
    }

    AnalyticAge = {
        "ID": "Data umur berhasil ditemukan",
        "EN": "Age data retrieved successfully",
    }

    AnalyticLocation = {
        "ID": "Data lokasi berhasil ditemukan",
        "EN": "Location data retrieved successfully",
    }

    AnalyticDevices = {
        "ID": "Data devices berhasil ditemukan",
        "EN": "Devices data retrieved successfully",
    }

    GetMessages = {
        "ID": "History Pesan berhasil ditemukan",
        "EN": "Message History retrieved successfully",
    }


    GetConclusion = {
        "ID": "Data conclusion berhasil ditemukan",
        "EN": "Conclusion data retrieved successfully",
    }

    GetListDocument = {
        "ID": "Data dokumen berhasil ditemukan",
        "EN": "Document data retrieved successfully",
    }

    CleanVectorDatabase = {
        "ID": "Database vector berhasil dibersihkan",
        "EN": "Vector database cleaned successfully",
    }

    @property
    def message(self):
        return self.value