from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random

from Jobs.models import CandidateProfile, RecruiterProfile, Job, Application, SavedJob

fake = Faker()


class Command(BaseCommand):
    help = "Create bulk dummy data"

    def handle(self, *args, **kwargs):

        candidates = []
        recruiters = []

        for i in range(20):
            username = f"candidate{i+1}"
            user, _ = User.objects.get_or_create(username=username)
            user.set_password("12345")
            user.email = f"{username}@gmail.com"
            user.first_name = fake.first_name()
            user.last_name = fake.last_name()
            user.save()

            CandidateProfile.objects.get_or_create(
                user=user,
                defaults={
                    "phone": str(random.randint(7000000000, 9999999999)),
                    "qualification": random.choice(["BSc", "MSc", "BCA", "MCA", "BE", "BTech"]),
                    "skills": random.choice([
                        "Python, Django, MySQL",
                        "HTML, CSS, JavaScript",
                        "SQL, MySQL, Excel",
                        "Java, Spring Boot",
                        "SAP Basis, SQL",
                    ]),
                }
            )

            candidates.append(user)

        for i in range(10):
            username = f"recruiter{i+1}"
            user, _ = User.objects.get_or_create(username=username)
            user.set_password("12345")
            user.email = f"{username}@company.com"
            user.first_name = fake.first_name()
            user.last_name = fake.last_name()
            user.save()

            RecruiterProfile.objects.get_or_create(
                user=user,
                defaults={
                    "company_name": fake.company(),
                    "phone": str(random.randint(7000000000, 9999999999)),
                    "company_location": random.choice(["Pune", "Mumbai", "Nagpur", "Bangalore", "Hyderabad"]),
                }
            )

            recruiters.append(user)

        job_titles = [
            "Python Developer",
            "Django Developer",
            "Backend Developer",
            "Frontend Developer",
            "Full Stack Developer",
            "SQL Developer",
            "Software Engineer",
            "Web Developer",
            "SAP Basis Trainee",
            "Data Analyst",
        ]

        jobs = []

        for i in range(30):
            recruiter = random.choice(recruiters)

            job = Job.objects.create(
                recruiter=recruiter,
                title=random.choice(job_titles),
                company=fake.company(),
                location=random.choice(["Pune", "Mumbai", "Nagpur", "Bangalore", "Hyderabad"]),
                salary=random.choice(["2 LPA", "3 LPA", "4 LPA", "5 LPA", "6 LPA"]),
                skills_required=random.choice([
                    "Python, Django, MySQL",
                    "HTML, CSS, JavaScript",
                    "SQL, MySQL",
                    "Java, Spring Boot",
                    "SAP Basis, Linux",
                ]),
                description=fake.paragraph(nb_sentences=5),
                status=random.choice(["Open", "Closed"]),
            )

            jobs.append(job)

        for i in range(50):
            Application.objects.get_or_create(
                candidate=random.choice(candidates),
                job=random.choice(jobs),
                defaults={
                    "status": random.choice(["Applied", "Shortlisted", "Rejected", "Selected"])
                }
            )

        for i in range(30):
            SavedJob.objects.get_or_create(
                candidate=random.choice(candidates),
                job=random.choice(jobs),
            )

        self.stdout.write(self.style.SUCCESS("Dummy data created successfully!"))