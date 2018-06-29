from unittest import TestCase
try:
	from unittest.mock import ANY, MagicMock, patch
except ImportError:
	from mock import ANY, MagicMock, patch
import pigpio

from hcsr501 import HcSr501

class HcSr501Test(TestCase):
	def __get_mock_pi(self, return_bool):
		mock = MagicMock()
		mock.read.return_value = return_bool
		return mock

	@patch.object(pigpio, 'pi')
	def test_active(self, mock):
		for i in [0, 1]:
			mock.return_value=self.__get_mock_pi(i)

			HCSR501 = HcSr501()
			self.assertEqual(bool(i), HCSR501.active)