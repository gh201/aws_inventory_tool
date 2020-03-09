import time

from django.test import TestCase

from frontend.elapsed_time_counter import ElapsedTime


class ElapsedTimeCounterTests(TestCase):

    timer = ElapsedTime()

    def test_counter_correct(self):

        self.timer.start_counting()
        time.sleep(1.5)
        self.timer.stop_counting()

        self.assertEqual(self.timer.get_seconds(), 1.5)
