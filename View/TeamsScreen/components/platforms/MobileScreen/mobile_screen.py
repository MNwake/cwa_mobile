from kivymd.uix.screen import MDScreen


class TeamsMobileScreen(MDScreen):
    pass
    # def utility_button(self):
    #     fake = Faker()
    #     for _ in range(100):
    #         # Create Rider
    #         rider = Rider(
    #             email=fake.email(),
    #             first_name=fake.first_name(),
    #             last_name=fake.last_name(),
    #             date_of_birth=fake.date_of_birth(minimum_age=5, maximum_age=60),
    #             gender=random.choice(['Male', 'Female']),
    #             stance=random.choice(['regular', 'goofy']),
    #             year_started=fake.random_int(min=1972, max=2018),  # Within the last 40 years
    #             home_park=random.choice(Park.objects().all())
    #         )
    #         rider.save()
    #         print('created rider')
    #
    #         # Create 100 Scorecards for the rider
    #         for _ in range(100):
    #             scorecard = Scorecard(
    #                 date=datetime.now(),
    #                 section=random.choice(['kicker', 'rail', 'air trick']),
    #                 division=random.uniform(1, 100),
    #                 execution=random.uniform(1, 100),
    #                 creativity=random.uniform(1, 100),
    #                 difficulty=random.uniform(1, 100),
    #                 score=random.uniform(1, 100),
    #                 landed=random.choice([True, False]),
    #                 park=rider.home_park,
    #                 rider=rider
    #             )
    #             scorecard.save()
    #             rider.scorecards.append(scorecard)
    #         print(_, 'created 100 scorecards for:', rider.full_name, )
    #         rider.save()

