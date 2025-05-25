class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")

        self.name = name
        self.pet_type = pet_type

        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            self.owner = owner
        else:
            self.owner = None

        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name={self.name} type={self.pet_type}>"

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

    def __repr__(self):
        return f"<Owner name={self.name}>"
