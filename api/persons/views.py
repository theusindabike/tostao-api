from rest_framework import generics


from api.persons.models import Person, PersonSerializer


class Persons(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
