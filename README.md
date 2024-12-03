# Homework for the "Asynchronous Processing" Module

## Welcome! 🧠

In the world of modern information technologies, processing large volumes of data requires efficient and rapid methods. The task ahead involves writing Python scripts: one employs asynchronous capabilities to sort files in folders, while the other utilizes the MapReduce paradigm to analyze word frequency in a text and visualize the results.

Completing this assignment will help develop skills in asynchronous programming and efficient file handling for large-scale data. Through this task, I have:

- Practiced using libraries for asynchronous programming and performance optimization, implementing asynchronous functions for recursive file reading and sorting;
- Applied Python's parallel processing capabilities to accelerate code execution.

Asynchronous processing has become an integral part of real-world programming projects. The ability to work efficiently with asynchronous code is essential for specialists dealing with large data volumes, high loads, and the need for real-time operations.

---

### Task 1

Write a Python script that reads all files in a user-specified source folder and distributes them into subfolders in the destination directory based on file extensions. The script should perform sorting asynchronously for more efficient handling of a large number of files.

#### Step-by-Step Instructions

1. Import the necessary asynchronous libraries.
2. Create an `ArgumentParser` object to handle command-line arguments.
3. Add required arguments to specify the source and target folders.
4. Initialize asynchronous paths for the source and target folders.
5. Write an asynchronous function, `read_folder`, that recursively reads all files in the source folder and its subfolders.
6. Write an asynchronous function, `copy_file`, that copies each file into the appropriate subfolder in the target folder based on its extension.
7. Configure error logging.
8. Run the `read_folder` asynchronous function in the main block.

---

### Task 2

Write a Python script that downloads text from a given URL, analyzes word frequency in the text using the MapReduce paradigm, and visualizes the top words with the highest frequency.

#### Step-by-Step Instructions

1. Import the necessary modules (`matplotlib`, among others).
2. Use the MapReduce implementation provided in the lecture notes.
3. Create a `visualize_top_words` function to visualize the results.
4. In the main code block, retrieve the text from the URL, apply MapReduce, and visualize the results.
