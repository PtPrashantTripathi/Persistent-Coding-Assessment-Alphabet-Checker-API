# Coding Assessment - Persistent Systems limited - Alphabet Checker API  

This project is a simple Flask API that checks if a given string contains all the letters of the English alphabet.
The input string is **case-insensitive**.
It supports both `GET` and `POST` methods.

## Code Structure  
- **`api.py`**: The main Flask application.  
- **`test.py`**: Script to test the API using various scenarios.  
- **`requirements.txt`**: File listing the required Python modules.  
- **`README.md`**: Documentation file.  

## Requirements  

- **Python Modules**:  
    - Flask  
    - Requests  

Install the required packages:  
```sh  
pip install -r requirements.txt
```  

## Running the API  

Start the Flask API server:  
```sh  
python api.py  
```  

The server will run on `http://localhost:3000`.  

## Running the Tests  

Run the test script:  
```sh  
python test.py  
```  

The script will execute test cases and print the results.  

## API Endpoints  

### **POST `/`**  
- **Description**: Checks if the provided `input_string` contains all the letters of the English alphabet.  
- **Request Body**: JSON object with the field `input_string`.  
- **Response**:  
    - **`200 OK`**:  
        ```json  
        {  
          "contains_all_alphabets": true/false  
        }  
        ```  
    - **`400 Bad Request`**:  
        ```json  
        {  
          "error": "Invalid input: input_string is required"  
        }  
        ```  

### **GET `/`**  
- **Description**: Checks if the provided `input_string` contains all the letters of the English alphabet.  
- **Query Parameters**:  
    - `input_string` (required): The string to check.  
- **Response**:  
    - **`200 OK`**:  
        ```json  
        {  
          "contains_all_alphabets": true/false  
        }  
        ```  
    - **`400 Bad Request`**:  
        ```json  
        {  
          "error": "Invalid input: input_string is required"  
        }  
        ```  

## Example Requests  

### POST Request  
```sh  
curl -X POST http://localhost:3000/ \  
-H "Content-Type: application/json" \  
-d '{"input_string": "The quick brown fox jumps over the lazy dog"}'  
```  

#### Response:  
- **`200 OK`**:  
```json  
{  
    "contains_all_alphabets": true  
}  
```  

### GET Request  
```sh  
curl "http://localhost:3000/?input_string=The%20quick%20brown%20fox%20jumps%20over%20the%20lazy%20dog"  
```  

#### Response:  
- **`200 OK`**:  
```json  
{  
    "contains_all_alphabets": true  
}  
```  
