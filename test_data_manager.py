import unittest
import data_manager


class TestDataManager(unittest.TestCase):

    def test_get_all_questions(self):
        answer = data_manager.get_all_questions()
        self.assertNotEqual(len(answer), 0)

    def test_get_question(self):
        answer = data_manager.get_question(1)
        self.assertEqual(answer['id'], 1)

    def test_get_answers_for_question(self):
        answer = data_manager.get_answers_for_question(1)
        self.assertEqual(answer[0]['question_id'], 1)

    def test_post_question(self):
        answer = data_manager.post_question('Test Title', 'Test Message')
        self.assertGreater(answer, 0)

    def test_get_answer(self):
        answer = data_manager.get_answer(1)
        self.assertEqual(answer['id'], 1)


    # DELETE_QUESTION_ID = test_post_question()
    #
    # def test_delete_question(self):
    #     time.sleep(1)
    #     question_id = DELETE_QUESTION_ID
    #     print(question_id)
    #     data_manager.delete_question(question_id)
    #     answer = data_manager.get_question(question_id)
    #     self.assertEqual(answer, None)


if __name__ == '__main__':
    unittest.main()
