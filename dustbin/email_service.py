from django.core.mail import send_mail
from django.conf import settings


def send_waste_email(waste_level, distance):

    subject = "🚨 Smart Dustbin Full Alert"

    message = f"""
🚨 SMART DUSTBIN ALERT 🚨

Bin 1 is FULL.

Waste Level: {waste_level:.1f}%
Distance: {distance:.1f} cm

Please empty the dustbin.
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],
        fail_silently=False,
    )

    print("Email alert sent successfully!")