from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from .models import WasteData
from .email_service import send_waste_email


def dashboard(request):
    latest_data = WasteData.objects.order_by("-created_at").first()

    return render(
        request,
        "dustbin/index.html",
        {
            "latest_data": latest_data
        }
    )


@csrf_exempt
def receive_sensor_data(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)

            bin_id = data.get("bin_id")
            distance = data.get("distance")
            waste_level = data.get("waste_level")
            status = data.get("status")

            # Get the previous reading for this bin
            previous_data = WasteData.objects.filter(
                bin_id=bin_id
            ).order_by("-created_at").first()

            # Save current sensor data
            WasteData.objects.create(
                bin_id=bin_id,
                distance=distance,
                waste_level=waste_level,
                status=status
            )

            # ------------------------------------------------
            # SEND EMAIL ONLY WHEN BIN CROSSES 80%
            # ------------------------------------------------

            if waste_level >= 80:

                # First reading is already 80% or more
                if previous_data is None:

                    send_waste_email(
                        waste_level,
                        distance
                    )

                # Previous reading was below 80%
                elif previous_data.waste_level < 80:

                    send_waste_email(
                        waste_level,
                        distance
                    )

            return JsonResponse({
                "success": True,
                "message": "Data received successfully",
                "waste_level": waste_level,
                "status": status
            })

        except Exception as e:

            return JsonResponse({
                "success": False,
                "error": str(e)
            }, status=400)

    return JsonResponse({
        "error": "Only POST requests are allowed"
    }, status=405)