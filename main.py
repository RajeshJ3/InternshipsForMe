from src.categories import CATEGORIES


class MakeUrl:
    URL = "https://internshala.com/internships/"
    work_from_home = False
    duration = False
    part_time_allowed = False
    with_job_offer = False
    asked_for_categories = False

    def ask_for_work_from_home(self):
        while True:
            work_from_home_input = input("\nWork from home (y/n): ")
            if work_from_home_input == 'y':
                self.URL += "work-from-home-"
                self.work_from_home = True
                break
            elif work_from_home_input == 'n':
                break
            else:
                print("Please answer y for yes, n for no")
        return self.work_from_home

    def ask_for_with_job_offer(self):
        while True:
            with_job_offer_input = input(
                "\nInternships with job offer (y/n): ")
            if with_job_offer_input == 'y':
                self.with_job_offer = True
                break
            elif with_job_offer_input == 'n':
                break
            else:
                print("Please answer y for yes, n for no")
        return self.with_job_offer

    def ask_for_part_time_allowance(self):
        while True:
            part_time_allowed_input = input(
                "\nInternships with part time (y/n): ")
            if part_time_allowed_input == 'y':
                self.part_time_allowed = True
                break
            elif part_time_allowed_input == 'n':
                break
            else:
                print("Please answer y for yes, n for no")
        return self.part_time_allowed

    def ask_for_duration(self):
        while True:
            duration_input = input(
                "\nDuration in months\nenter either 1, 2, 3, 4, 6, 12, 24 or just press enter for any\n--> ")
            if duration_input == "":
                break
            elif duration_input == "1":
                self.duration = 1
            elif duration_input == "2":
                self.duration = 2
            elif duration_input == "3":
                self.duration = 3
            elif duration_input == "4":
                self.duration = 4
            elif duration_input == "6":
                self.duration = 6
            elif duration_input == "12":
                self.duration = 12
            elif duration_input == "24":
                self.duration = 24
            else:
                print("Invalid Input")
                continue
            break
        return self.duration

    def ask_for_categories(self):
        print("Please Select categories: ")
        for index, category in enumerate(CATEGORIES.items()):
            print(f"{index+1}. {category[0]}")

        while True:
            try:
                input_categories = input("\nEnter choices (1,2,3...): ")
                input_categories = input_categories.replace(' ', '').split(',')
                user_selected_categories = []
                for i in input_categories:
                    id = int(i)
                    if id > len(CATEGORIES):
                        raise Exception
                    user_selected_categories.append(id)

                for index, category in enumerate(CATEGORIES.items()):
                    if index + 1 in user_selected_categories:
                        self.URL += f"{category[1]},"
                self.URL = self.URL[:-1] + \
                    "-jobs/" if self.work_from_home else self.URL[:-
                                                                  1] + "-internship/"
                self.asked_for_categories = True
                break

            except:
                print("Please enter valid number(s)")

    def get_url(self):
        if self.duration:
            self.URL += f"duration-{self.duration}/"

        if self.part_time_allowed:
            self.URL += f"part_time-true/"

        if self.with_job_offer:
            self.URL += f"ppo-true/"

        if self.work_from_home and not self.asked_for_categories:
            self.URL = self.URL[:self.URL.index('work-from-home-')+15] + \
                "jobs/" + self.URL[self.URL.index('work-from-home-')+15:]

        return self.URL


make_url = MakeUrl()

make_url.ask_for_work_from_home()

make_url.ask_for_with_job_offer()

make_url.ask_for_part_time_allowance()

make_url.ask_for_duration()

make_url.ask_for_categories()

print(
    f"\nHere's the your URL for internships based on your preferences:\n\n{make_url.get_url()}\n\n")
