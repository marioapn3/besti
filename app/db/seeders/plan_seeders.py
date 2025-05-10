
from app.db.database import plan_collection
import datetime

async def seed_plans():
    admin_data = [
          {
            "name": "Founders",
            "description": "Founders Business",
            "pricing_model": "Fixed",
            "price" : 3000.0,
            "feature_quotas": {
                "sources" : {
                    "quota": 500000,
                    "used": 0
                },
                "datasets" : {
                    "quota": 500000,
                    "used": 0
                },
                "messages" :{
                    "quota": 500000,
                    "used": 0
                },
                "persona_system" : 3,
                
                "documents_per_month": 50,
                "integrations": 15,
                "team_members": 15,
                "organisation": 3
            },
            "billing_cycle": "Monthly",
            "type": "plan",
        },
        {
            "name": "SMB",
            "description": "Small and Medium Business",
            "pricing_model": "Fixed",
            "price" : 1000.0,
            "feature_quotas": {
                 "sources" : {
                    "quota": 500000,
                    "used": 0
                },
                "datasets" : {
                    "quota": 500000,
                    "used": 0
                },
                "messages" :{
                    "quota": 500000,
                    "used": 0
                },
                "persona_system" : 8,

                "documents_per_month": 500,
                "integrations": 5,
                "team_members": 5,
                "organisation": 2
            },
            "trial_enabled": True,
            "trial_duration_days": 30,
            "billing_cycle": "Monthly",
            "type": "plan",
        },
        {
            "name": "Enterprise",
            "description": "Enterprise Business",
            "pricing_model": "Fixed",
            "price" : 2000.0,
            "feature_quotas": {
                  "sources" : {
                    "quota": 500000,
                    "used": 0
                },
                "datasets" : {
                    "quota": 500000,
                    "used": 0
                },
                "messages" :{
                    "quota": 500000,
                    "used": 0
                },
                "persona_system" : 10,

                "documents_per_month": 200,
                "integrations": 10,
                "team_members": 10,
                "organisation": 1
            },
            # "trial_enabled": True,
            # "trial_duration_days": 30,
            "billing_cycle": "Monthly",
            "type": "plan",
        },
      
        # free trial
        {
            "name": "Trial",
            "description": "Trial Business",
            "pricing_model": "Fixed",
            "price" : 0.0,
            "feature_quotas": {
                "sources" : {
                    "quota": 500000,
                    "used": 0
                },
                "datasets" : {
                    "quota": 500000,
                    "used": 0
                },
                "messages" :{
                    "quota": 500000,
                    "used": 0
                },
                "persona_system" : 1,

                "documents_per_month": 10,
                "integrations": 1,
                "team_members": 1,
                "organisation": 1
            },
            "trial_enabled": True,
            "trial_duration_days": 7,
            "billing_cycle": "Weekly",

            "type": "plan",
        },

        # 1 credits datasets
        {
            "name": "1 Credits Datasets",
            "description": "1 Credits Datasets = 1 Million Tokens",
            "pricing_model": "Fixed",
            "price" : 1000.0,
            "feature_quotas": {
                "datasets" : {
                    "quota" : 1000000,
                }
            },
            "type": "credits",
        },

         # 1 credits datasources
        {
            "name": "1 Credits DataSources",
            "description": "1 Credits DataSources = 1 Million Characters",
            "pricing_model": "Fixed",
            "price" : 1000.0,
            "feature_quotas": {
                "sources" : {
                    "quota" : 1000000,
                }
            },
            "type": "credits",
        },

         # 1 credits chats
        {
            "name": "1 Credits Chats Token",
            "description": "1 Credits Chats = 1 Million Tokens",
            "pricing_model": "Fixed",
            "price" : 1000.0,
            "feature_quotas": {
                "messages" : {
                    "quota" : 1000000,
                }
            },
            "type": "credits",
        },
    ]

    if plan_collection.count_documents({}) == 0:
        plan_collection.insert_many(admin_data)