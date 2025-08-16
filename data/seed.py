import asyncio
from datetime import date
from db_setup import init_db
from models.clinic_models import DentalClinic
from models.dentist_models import Dentist
from models.user_models import User
from models.common_models import Address, SpecialtyCost


async def seed_data():
    await init_db()
    print("Database initialized, starting to seed data...")

    # --- Seed Clinics ---
    clinic_1 = DentalClinic(
        name="Smile Studio Delhi",
        dentists=[],  # To be filled later
        address=Address(
            street="123 New Street", city="New Delhi", state="Delhi", pincode="110001"
        ),
        rating=4.8,
        email="smilestudio@example.com",
    )
    clinic_2 = DentalClinic(
        name="Global Dental Care",
        dentists=[],
        address=Address(
            street="456 Gurugram Road",
            city="Gurugram",
            state="Haryana",
            pincode="122001",
        ),
        rating=4.5,
        email="globaldental@example.com",
    )
    await DentalClinic.insert_many([clinic_1, clinic_2])
    clinic_1_id = clinic_1.clinic_id
    clinic_2_id = clinic_2.clinic_id

    # --- Seed Dentists ---
    dentist_1 = Dentist(
        clinic_id=clinic_1_id,
        first_name="Dr. Jane",
        last_name="Doe",
        specialties=["implants", "root canal"],
        years_of_experience=15,
        languages_spoken=["English", "Hindi"],
        rating=4.9,
        # Updated to a dictionary to match the new model
        cost={
            "implants": SpecialtyCost(
                specialty="implants", cost_min=1000, cost_max=1500
            ),
            "root canal": SpecialtyCost(
                specialty="root canal", cost_min=700, cost_max=1200
            ),
        },
        availability=[date(2025, 9, 10), date(2025, 9, 11), date(2025, 9, 12)],
    )
    dentist_2 = Dentist(
        clinic_id=clinic_1_id,
        first_name="Dr. John",
        last_name="Smith",
        specialties=["cosmetic", "veneers"],
        years_of_experience=10,
        languages_spoken=["English", "Hindi"],
        rating=4.7,
        # Updated to a dictionary to match the new model
        cost={
            "cosmetic": SpecialtyCost(
                specialty="cosmetic", cost_min=800, cost_max=1200
            ),
            "veneers": SpecialtyCost(specialty="veneers", cost_min=1500, cost_max=2000),
        },
        availability=[date(2025, 9, 15), date(2025, 9, 16)],
    )
    dentist_3 = Dentist(
        clinic_id=clinic_2_id,
        first_name="Dr. Emily",
        last_name="White",
        specialties=["root canal", "crowns"],
        years_of_experience=8,
        languages_spoken=["English", "Spanish"],
        rating=4.5,
        # Updated to a dictionary to match the new model
        cost={
            "root canal": SpecialtyCost(
                specialty="root canal", cost_min=700, cost_max=1000
            ),
            "crowns": SpecialtyCost(specialty="crowns", cost_min=500, cost_max=800),
        },
        availability=[date(2025, 9, 20), date(2025, 9, 21)],
    )
    await Dentist.insert_many([dentist_1, dentist_2, dentist_3])

    # Update clinic documents with dentist IDs
    clinic_1.dentists = [dentist_1.dentist_id, dentist_2.dentist_id]
    await clinic_1.save()

    clinic_2.dentists = [dentist_3.dentist_id]
    await clinic_2.save()

    # --- Seed Users ---
    user_1 = User(
        anonymized_id="hashed_user_id_1",  # User model expects anonymized_id, not id
        email="testuser1@example.com",
        password_hash="hashed_password_1",
        dental_needs=["implants", "veneers"],
        preferences={"budget": 3000, "travel_style": "relaxed"},
        interests=["history", "yoga"],
        travel_dates={"start": date(2025, 9, 1), "end": date(2025, 9, 20)},
    )
    await user_1.insert()

    print("Database seeding completed!")


if __name__ == "__main__":
    asyncio.run(seed_data())
