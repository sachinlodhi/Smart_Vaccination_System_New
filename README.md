
# Automated Aadhar-based Vaccination Registration System

![Application Demo](![WhatsApp Image 2023-08-22 at 11 56 20 PM (1)](https://github.com/sachinlodhi/Smart_Vaccination_System_New/assets/28351261/88175342-4143-430c-92a8-4a0c288b7230)
)![WhatsApp Image 2023-08-22 at 11 56 35 PM](https://github.com/sachinlodhi/Smart_Vaccination_System_New/assets/28351261/c5175e92-5990-492f-8aa9-9f25d8566825)


## Overview

This Python application utilizes the Tesseract OCR module to extract the Aadhar number from an input image of an Aadhar Card. It then interacts with a database to check whether the extracted Aadhar number has been registered for vaccination. If not, the application proceeds to register the individual for vaccination and issues a token for the vaccination process. The token number is displayed on the screen, streamlining the registration and token issuance process during the Covid vaccination drive.

## Features

- Automated Aadhar number extraction using Tesseract OCR.
- Integration with a database to check vaccination registration status.
- On-the-spot registration and token issuance for unregistered individuals.
- Real-time token display for the next vaccination candidate.

## Motivation

This application was developed in response to the challenges posed by the manual vaccination registration and token issuance process during the Covid vaccination drive in India. The manual process was time-consuming and often led to long queues and inefficiencies. This automated system aims to eliminate human intervention in the registration and token issuance process, thus optimizing the vaccination drive and ensuring a smoother experience for both healthcare providers and recipients.

## How to Use

1. **Prerequisites**: Ensure you have Python installed on your system along with the necessary libraries. Install the required packages using the following command:

   ```
   pip install -r requirements.txt
   ```

2. **Database Setup**: Set up the database connection by providing the necessary credentials in the `config.py` file.

3. **Running the Application**: Execute the following scripts to start the application:

   ```
   python database.py
   python using_tesseract.py
   python app.py
   ```

4. **Image Input**: Provide an input image of an Aadhar Card to the application. The application will process the image and extract the Aadhar number using Tesseract OCR.

5. **Registration and Token**: The application will then check the database to determine if the extracted Aadhar number is registered for vaccination. If not, it will proceed to register the individual and assign a token number.

6. **Token Display**: The token number will be displayed on the screen, indicating the next candidate in line for vaccination.

## Contributing

Contributions to this project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to express our gratitude to the healthcare workers and volunteers who are tirelessly working towards mass vaccination during the Covid pandemic. This application is a small contribution to their efforts.
