from unittest import TestCase
from phonebook import Phonebook


class TestPhonebook(TestCase):
    def setUp(self):
        self.phonebook = Phonebook()

    def test_save_contact(self):
        self.phonebook.save_contact("Jumoke","0606758")
        self.assertEqual({"Jumoke":"0606758"},self.phonebook.contacts)

    def test_display_contacts(self):
        self.phonebook.save_contact("Jumoke","0904567")
        self.assertEqual("Jumoke : 0904567\n",self.phonebook.display_contacts())
        self.assertEqual({"Jumoke": "0606758"}, self.phonebook.contacts)

    def test_delete_contact(self):
        self.phonebook.save_contact("Jumoke", "0606758")
        self.phonebook.delete_contact("Jumoke")
        self.assertEqual({}, self.phonebook.contacts)


    def test_search_contact_by_name(self):
        self.phonebook.save_contact("Jumoke", "0606758")
        self.assertEqual("0606758",self .phonebook.search_contact("Jumoke"))
        self.assertEqual({"Jumoke": "0606758"}, self.phonebook.contacts)

    def test_search_contact_by_name(self):
        self.phonebook.save_contact("Jumoke", "0606758")
        self.assertEqual("Jumoke", self.phonebook.search_contact("0606758"))
        self.assertEqual({"Jumoke": "0606758"}, self.phonebook.contacts)


    def test_update_contact(self):
        self.phonebook.save_contact("Jumoke", "0606758")
        self.assertEqual({"Jumoke": "0606758"}, self.phonebook.contacts)
        
