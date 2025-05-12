import spacy
import os
import re
import logging
from docx import Document
import chardet


class DataPreprocessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.processed_files = []
        self.failed_files = []
        self.nlp = spacy.load("ru_core_news_sm")

    def get_file_encoding(self, file_path):
        """
        Определяем кодировку и открываем файл с нужной кодировкой.
        Если не удается определить кодировку, по умолчанию возвращаем 'windows-1251' для русского текста.
        """
        print(
            f"Определяем кодировку файла: {file_path}"
        )  # Выводим имя файла для отладки
        # Используем chardet для определения кодировки
        try:
            with open(file_path, "rb") as f:
                raw_data = f.read()
                result = chardet.detect(raw_data)
                encoding = result["encoding"]

                # Если кодировка не определена, возвращаем 'windows-1251' как кодировку по умолчанию для русскоязычных текстов
                if encoding is None:
                    encoding = "windows-1251"

                return encoding
        except Exception as e:
            logging.error(f"Ошибка при определении кодировки файла {file_path}: {e}")
            return (
                "windows-1251"  # Возвращаем 'windows-1251' по умолчанию в случае ошибки
            )

    def clean_text(self, text):
        """
        Очищаем текст от лишних символов и приводим к нужному виду.
        """
        try:
            text = re.sub(r"\s+", " ", text)  # Убираем множественные пробелы
            # text = re.sub(r"[^\x00-\x7F]+", " ", text)  # Убираем не-ASCII символы
            text = (
                text.strip().lower()
            )  # Преобразуем в нижний регистр и убираем лишние пробелы
            return text
        except Exception as e:
            logging.error(f"Ошибка при очистке текста: {e}")
            return None

    def tokenize_and_lemmatize(self, text):
        """
        Токенизируем и лемматизируем текст с помощью spaCy.
        """
        try:
            doc = self.nlp(text)
            lemmatized_tokens = [token.lemma_ for token in doc]
            return " ".join(lemmatized_tokens)
        except Exception as e:
            logging.error(f"Ошибка при токенизации и лемматизации текста: {e}")
            return None

    def process_file(self, file_path):
        """
        Читаем файл (PDF, DOCX, FB2, HTML, RTF, DOC), очищаем и токенизируем/лемматизируем текст.
        """
        try:
            print(f"Обрабатываем файл: {file_path}")  # Выводим имя файла для отладки
            text = None

            if file_path.lower().endswith(".docx"):
                # Use python-docx to extract text from docx files
                doc = Document(file_path)
                text = "\n".join([para.text for para in doc.paragraphs])
            else:
                # Пробуем открыть и обработать файл с учетом его кодировки
                encoding = self.get_file_encoding(file_path)
                with open(file_path, "r", encoding=encoding, errors="ignore") as file:
                    text = file.read()

            if text:
                cleaned_text = self.clean_text(text)
                if cleaned_text is None:
                    logging.error(
                        f"Ошибка очистки текста файла {file_path}. Пропускаем файл."
                    )
                    self.failed_files.append(file_path)
                    return

                processed_text = self.tokenize_and_lemmatize(cleaned_text)
                if processed_text is None:
                    logging.error(
                        f"Ошибка обработки текста файла {file_path}. Пропускаем файл."
                    )
                    self.failed_files.append(file_path)
                    return

                output_file_path = os.path.join(
                    self.output_dir, os.path.basename(file_path) + ".txt"
                )
                with open(output_file_path, "w", encoding="utf-8") as output_file:
                    output_file.write(processed_text)

                self.processed_files.append(file_path)

        except Exception as e:
            logging.error(f"Ошибка при обработке файла {file_path}: {e}")
            self.failed_files.append(file_path)

    def process_files(self):
        """
        Процесс обработки всех файлов в директории.
        """
        files = os.listdir(self.input_dir)
        processed_count = 0
        failed_count = 0

        if not files:
            print("Папка пуста или нет файлов для обработки.")
            return

        print(f"Найдено файлов: {len(files)}")

        for file_name in files:
            print(f"Обрабатываем файл: {file_name}")  # Выводим имя файла для отладки
            file_path = os.path.join(self.input_dir, file_name)
            try:
                if (
                    file_name.endswith(".pdf")
                    or file_name.endswith(".docx")
                    or file_name.endswith(".fb2")
                    or file_name.endswith(".html")
                    or file_name.endswith(".htm")
                    or file_name.endswith(".rtf")
                ):
                    self.process_file(file_path)
                    processed_count += 1
                    print(f"Файл {file_name} обработан успешно!")
                else:
                    logging.warning(
                        f"Файл {file_name} не поддерживаемого формата (не pdf, docx, fb2, html, rtf). Пропускаем."
                    )
                    print(f"Файл {file_name} не поддерживаемого формата.")
            except Exception as e:
                logging.error(f"Не удалось обработать файл {file_name}. Ошибка: {e}")
                failed_count += 1

        print(f"\nОбработано файлов: {processed_count}")
        print(f"Не удалось обработать файлов: {failed_count}")
        print(f"Обработанные файлы: {', '.join(self.processed_files)}")
        print(f"Ошибки записаны в 'preprocessing_errors.log'.")


# Создаем объект DataPreprocessor
if __name__ == "__main__":

    # Папка с файлами PDF, DOCX, FB2, HTML, RTF, DOC
    # Папка для сохранения текстов
    input_folder = "/Users/slava/Work/Python-Preparations/files"  # Папка с файлами PDF, DOCX, FB2, HTML, RTF, DOC
    output_folder = "/Users/slava/Work/Python-Preparations/files_output"  # Папка для сохранения текстов

    data_preprocessor = DataPreprocessor(input_folder, output_folder)

    # Запускаем обработку файлов
    data_preprocessor.process_files()
