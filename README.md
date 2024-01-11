	
Hospital Management System - Project Requirement Document

1. Introduction

1.1 Purpose
The purpose of the Hospital Management System is to provide an efficient solution for managing hospital operations. This system aims to organise the processes involved in hospital management, including the creation and management of hospitals, departments, patients, and their respective statuses.

1.2 Scope
The scope of the Hospital Management System encompasses the creation of a superuser interface for overall management, allowing the addition of new hospitals, departments, and patients. The system will also provide functionalities to update patient status, manage and retrieve relevant information for administrative purposes.

2. System Requirements

2.1 Functional Requirements
1. Superuser Management:
Creation and management of a superuser with privileges to administer all system    operations.
   
2. Hospital Configuration:
Onboarding process to add new hospitals with details such as name, address, and a list of departments.

3. Department Management:
Ability to define and manage departments within each hospital.

4. Patient Management:
Creation of a new patient with an auto-incremented ID.
Recording patient details including hospital, disease, doctor name, and status (primary check, consultation, discharged, admitted, referred).

5. Patient Status Update:
Admin interface to update patient status (discharged, admitted) and record medication with remarks.

6. Patient Information Retrieval:
API to retrieve the current status of a patient using their name.
API to retrieve details of all hospital visits, date-wise, and their final status based on the most recent date.

2.2 Non-functional Requirements
1. Security:
Implement user authentication and authorization of the super user or admin  to ensure secure access to the system.

2. User Interface:
User Interface to add hospitals , patients and also to display the details of the patients and hospitals.


3. System Architecture
The Hospital Management System will be developed using the Django web framework, following the Model-View-Controller (MVC) architectural pattern. The architecture will include:

1.Database:
Utilise an MySQL to store information related to hospitals, departments, patients, and their statuses.

2.Backend:
Implement business logic and data processing using Django's built in backend capabilities.

3.APIs:
Implement RESTful APIs to facilitate communication between different system components.

4.Authentication and Authorization:
Utilize Django's built-in authentication and authorization mechanisms to control access to system features.
