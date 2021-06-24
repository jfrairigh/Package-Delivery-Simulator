# Time Complexity: O(1)
# Space Complexity: O(1)
class Package:
    def __init__(self, id, address, city, state, zip, deadline, kilo, notes, delivery_status):
        self._id = int(id)
        self._address = address
        self._city = city
        self._state = state
        self._zip = zip
        self._deadline = deadline
        self._kilo = kilo
        if len(notes) == 0:
            self._notes = 'no notes'
        elif len(notes) > 0:
            self._notes = notes
        self._delivery_status = delivery_status

    @property
    def id(self):
        return self._id

    @property
    def address(self):
        return self._address

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def zip(self):
        return self._zip

    @property
    def deadline(self):
        return self._deadline

    @property
    def kilo(self):
        return self._kilo

    @property
    def notes(self):
        return self._notes

    @property
    def delivery_status(self):
        return self._delivery_status

    def set_address(self, new_address):
        self._address = new_address

    def set_city(self, new_city):
        self._city = new_city

    def set_zip(self, new_zip):
        self._zip = new_zip

    def set_deadline(self, new_deadline):
        self._deadline = new_deadline

    def set_kilo(self, new_kilo):
        self._kilo = new_kilo

    def set_notes(self, new_note):
        self._note = new_note

    def set_delivery_status(self, new_delivery_status):
        self._delivery_status = new_delivery_status

    def __str__(self):
        return str(self._id) + " ," + self._address + " ," + self._city + " ," + self._state + " ," + self._zip + " ," + self._deadline + " ," + self._kilo + " ," + self._notes + ", " + self.delivery_status
