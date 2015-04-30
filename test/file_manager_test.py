# test_file_manager.py
# author: Josue Mendoza
# date: 4-2-2015

import unittest
import os
from file_manager import File
from logger import Logger

class FileManagerTest(unittest.TestCase):
    TEST_FOLDER = os.getcwd() + '\\test_folder'
    TEST_FILE = TEST_FOLDER + '\\test_file.txt'
    SAMPLE_CONTENT = 'sample text'
    SAMPLE_CONTENT_2 = 'another text sample'

    if not os.path.exists(TEST_FOLDER):
        os.makedirs(TEST_FOLDER)
    
    """Instantiate logger"""
    global logger
    logger =  Logger("log/")

    def test_file_manager_overwrites_file_content_of_an_existent_file(self):
        file_instance = File(self.TEST_FILE)

        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

        try:
            fo = open(self.TEST_FILE, "wb")
            fo.write(self.SAMPLE_CONTENT_2)            
        except IOError:
            logger.error("cannot write content to file")
        finally:
            fo.close()

        file_instance.write_content(self.SAMPLE_CONTENT)

        try:
            fo = open(self.TEST_FILE)
            file_content = fo.read()
        except IOError:
            logger.error("cannot read file")
        finally:
            fo.close()

        self.assertEqual(self.SAMPLE_CONTENT, file_content)
        file_instance.delete()

    def test_file_manager_creates_a_file_if_the_file_does_not_exist_while_writting_content(self):
        file_instance = File(self.TEST_FILE)

        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

        file_instance.write_content(self.SAMPLE_CONTENT)
        self.assertTrue(os.path.exists(self.TEST_FILE))
        file_instance.delete()

    def test_file_manager_can_read_file_content(self):
        file_instance = File(self.TEST_FILE)

        try:
            fo = open(self.TEST_FILE, "wb")
            fo.write(self.SAMPLE_CONTENT)
        except IOError:
            logger.error("cannot write content to file")           
        finally:
            fo.close()

        self.assertEqual(self.SAMPLE_CONTENT, file_instance.read_content())
        file_instance.delete()

    def test_file_manager_can_delete_its_file(self):
        file_instance = File(self.TEST_FILE)

        try:
            fo = open(self.TEST_FILE, "wb")
            fo.write('d')
        except IOError:
            logger.error("cannot write content to file")           
        finally:
            fo.close()

        self.assertTrue(os.path.exists(self.TEST_FILE))
        file_instance.delete()
        self.assertFalse(os.path.exists(self.TEST_FILE))

    def test_file_manager_can_tell_if_a_file_exists(self):
        file_instance = File(self.TEST_FILE)

        try:
            fo = open(self.TEST_FILE, "wb")
            fo.write('d')
        except IOError:
            logger.error("cannot write content to file")
        finally:
            fo.close()

        if os.path.exists(self.TEST_FILE):
            self.assertTrue(file_instance.file_exists())
        else:
            self.fail('problems validating existence of a file')
            logger.error("problems validating existence of a file")

        os.remove(self.TEST_FILE)

        if not os.path.exists(self.TEST_FILE):
            self.assertFalse(file_instance.file_exists())
        else:
            logger.error("problems validating existence of a file")
            self.fail('problems validating existence of a file')
