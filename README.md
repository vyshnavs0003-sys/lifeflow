# LifeFlow – Blood Bank Management System

## Project Overview
LifeFlow is a Django-based blood bank management system designed to connect donors, hospitals, and users through a structured and efficient workflow.

The system simulates a real-world blood donation ecosystem where users can register, request blood, manage donor profiles, and hospitals can handle blood inventory and blood request approvals.

---

## Features

### User Features
- User registration and authentication
- Option to become a donor
- View and update donor profile
- Request blood from hospitals
- Track blood request status
- View available donors
- Check blood availability based on blood group

### Hospital Features
- Hospital dashboard
- Manage blood inventory (add, update, delete)
- View incoming blood requests
- Approve, reject, or mark requests as completed
- Access donor list

### Authentication and Roles
- Built using Django authentication system
- Role-based access using UserProfile
  - USER
  - HOSPITAL

---

## Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap 5
- Database: SQLite
- Authentication: Django built-in authentication system
- Styling: Bootstrap with custom CSS
- Template Engine: Django Template Language

---

## How the System Works

The application follows a simple workflow:

1. Users register and log in to the system.
2. A user can choose to register as a donor or remain a regular user.
3. Hospitals manage their blood inventory by adding available blood units.
4. Users can submit blood requests to hospitals.
5. Hospitals review each request and update its status:
   - Pending
   - Approved
   - Completed or Rejected
6. Donor listings and blood availability are displayed based on filters such as blood group.

---

## Key Models

### UserProfile
Extends the default Django User model to store user roles. This helps separate hospital users from normal users without modifying the default authentication system.

### Donor
Stores donor-related information such as blood group, age, location, medical history, and availability status.

### Hospital
Represents hospital accounts and stores basic hospital information.

### BloodInventory
Tracks the availability of different blood groups in each hospital.

### BloodRequest
Handles the full lifecycle of a blood request from creation to completion, including status tracking.

---

## Key Design Decisions

One of the main decisions in this project was to keep the default Django User model unchanged and extend it using a separate UserProfile model. This made authentication simpler while still allowing role-based access control.

Relationships between models were carefully designed using ForeignKey and OneToOneField to reflect real-world connections. For example, each donor is directly linked to a user account, and each hospital manages its own blood inventory.

CASCADE delete behavior was used so that related data is automatically cleaned up when a parent record is removed. This helped maintain database consistency without manual cleanup logic.

Django ModelForms were used to reduce repetitive form handling code and speed up development. In views, function-based views were preferred for clarity and easier understanding of request flow.

On the frontend, a hybrid approach of Bootstrap and custom CSS was used. Bootstrap handled responsiveness, while custom CSS was used to maintain consistent branding and layout control.

After login, users are redirected based on their role, which ensures that hospitals and normal users experience different dashboards tailored to their needs.

---

## Assumptions Made During Development

The system assumes that each user belongs to only one role, either a normal user or a hospital. This simplifies authentication and avoids complex permission handling.

Hospitals are treated as special user accounts rather than separate authentication systems. This allows both users and hospitals to use the same login system.

Blood inventory is fully managed by hospitals, and normal users do not directly modify it.

Donor registration is optional and depends on user choice. Not every user in the system is expected to be a donor.

Contact information for donors is displayed only if the donor has explicitly allowed it, respecting privacy preferences.

Blood requests are handled manually by hospitals rather than being automatically processed, as this reflects a more realistic real-world workflow.

---

## Future Improvements

- REST API integration using Django REST Framework
- Email and SMS notification system for requests and approvals
- Location-based donor search
- Pagination for large datasets
- Improved security by replacing GET-based status updates with POST requests
- Analytics dashboard for hospitals
- Real-time updates for blood availability

---

## Learning Outcome

This project helped in understanding practical Django development, including:

- Working with authentication and role-based access control
- Designing relational database models using Django ORM
- Handling CRUD operations using ModelForms
- Structuring views for real-world workflows
- Implementing template inheritance and reusable UI components
- Building responsive interfaces using Bootstrap
- Understanding full-stack application flow from database to UI
