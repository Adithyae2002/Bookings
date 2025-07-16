from django import forms

from. models import Bookings

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'

        widgets ={
            'booking_date' : DateInput(),
        }
        labels ={
            'p_name':"Patient Name:",
            'p_phone':"Patient Phone:",
            'p_email': "Patient Email:",
            'doc_name': "Doctor name:",
            'booking_date':"Booking Date:",
        }