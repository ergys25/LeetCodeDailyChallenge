# Venue Booking Platform Project Plan

## Technology Stack
- **Backend**: Java 17, Spring Boot
- **Frontend**: Angular
- **Database**: PostgreSQL

## Project Duration
- **Duration**: 5 months (20 weeks)

---

## Backend Development

### Entity-Relationship Diagram (ERD)

```plaintext
[User]
- id (PK)
- email
- password_hash
- first_name
- last_name
- role
- created_at
- updated_at

[Venue]
- id (PK)
- name
- location
- capacity
- amenities
- status
- created_at
- updated_at

[Booking]
- id (PK)
- user_id (FK -> User)
- venue_id (FK -> Venue)
- date
- time
- status
- created_at
- updated_at

[Review]
- id (PK)
- user_id (FK -> User)
- venue_id (FK -> Venue)
- rating
- comment
- created_at
- updated_at

[Payment]
- id (PK)
- user_id (FK -> User)
- booking_id (FK -> Booking)
- amount
- status
- payment_date
- created_at
- updated_at




## Table: users

| Column       | Type          | Constraints                          |
|--------------|---------------|--------------------------------------|
| id           | SERIAL        | PRIMARY KEY                          |
| email        | VARCHAR(255)  | UNIQUE, NOT NULL                     |
| password_hash| VARCHAR(255)  | NOT NULL                             |
| first_name   | VARCHAR(255)  |                                      |
| last_name    | VARCHAR(255)  |                                      |
| role         | VARCHAR(50)   | NOT NULL                             |
| created_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |
| updated_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |

---

## Table: venues

| Column       | Type          | Constraints                          |
|--------------|---------------|--------------------------------------|
| id           | SERIAL        | PRIMARY KEY                          |
| name         | VARCHAR(255)  | NOT NULL                             |
| location     | VARCHAR(255)  |                                      |
| capacity     | INT           |                                      |
| amenities    | TEXT[]        |                                      |
| status       | VARCHAR(50)   | NOT NULL                             |
| created_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |
| updated_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |

---

## Table: bookings

| Column       | Type          | Constraints                          |
|--------------|---------------|--------------------------------------|
| id           | SERIAL        | PRIMARY KEY                          |
| user_id      | INT           | REFERENCES users(id)                 |
| venue_id     | INT           | REFERENCES venues(id)                |
| date         | DATE          |                                      |
| time         | TIME          |                                      |
| status       | VARCHAR(50)   | NOT NULL                             |
| created_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |
| updated_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |

---

## Table: reviews

| Column       | Type          | Constraints                          |
|--------------|---------------|--------------------------------------|
| id           | SERIAL        | PRIMARY KEY                          |
| user_id      | INT           | REFERENCES users(id)                 |
| venue_id     | INT           | REFERENCES venues(id)                |
| rating       | INT           |                                      |
| comment      | TEXT          |                                      |
| created_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |
| updated_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |

---

## Table: payments

| Column       | Type          | Constraints                          |
|--------------|---------------|--------------------------------------|
| id           | SERIAL        | PRIMARY KEY                          |
| user_id      | INT           | REFERENCES users(id)                 |
| booking_id   | INT           | REFERENCES bookings(id)              |
| amount       | DECIMAL(10, 2)| NOT NULL                             |
| status       | VARCHAR(50)   | NOT NULL                             |
| payment_date | TIMESTAMP     |                                      |
| created_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |
| updated_at   | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP            |





# Use Cases and User Stories

## Week 1-2: Setup and User Management

### US1: Setup Spring Boot project with Java 17

**Tasks:**

- Initialize Spring Boot project with Spring Initializr
- Configure build tools (Maven), dependencies, and project structure

**Acceptance Criteria:**

- Project structure created
- Dependencies configured

**Estimated Time:** 1 week

### US2: Implement User Registration

**Tasks:**

- Create User Entity and UserRepository
- Implement UserService with `registerUser()` method
- Implement registration endpoint (POST /api/users/register)

**Acceptance Criteria:**

- Users can register with valid email and password
- Passwords are securely hashed before storing

**Estimated Time:** 1 week

### US3: Implement User Login and JWT Authentication

**Tasks:**

- Implement login endpoint (POST /api/users/login)
- Generate JWT token upon successful login
- Implement JWT authentication filter and security configuration

**Acceptance Criteria:**

- Users can login with valid credentials
- JWT token is generated and used for authentication

**Estimated Time:** 1 week

### US4: Implement User Profile and Password Recovery

**Tasks:**

- Implement `getProfile()` and `updateProfile()` methods in UserService
- Create endpoints for getting and updating user profile (GET /api/users/{id}, PUT /api/users/{id})
- Implement password recovery functionality with email verification

**Acceptance Criteria:**

- Users can view and update their profile
- Users can recover their password via email

**Estimated Time:** 1 week

## Week 3-5: Venue Management

### US5: Implement Venue CRUD Operations

**Tasks:**

- Create Venue Entity and VenueRepository
- Implement VenueService with CRUD methods
- Implement CRUD endpoints for venues (POST/GET/PUT/DELETE /api/venues)

**Acceptance Criteria:**

- Venues can be created, read, updated, and deleted

**Estimated Time:** 3 weeks

### US6: Implement Venue Status Management

**Tasks:**

- Implement endpoints for venue cancellation (PUT /api/venues/{id}/cancel)
- Update Venue Entity and Service to support venue status management

**Acceptance Criteria:**

- Venue status can be updated and canceled

**Estimated Time:** 1 week

### US7: Implement Venue Calendar

**Tasks:**

- Create CalendarService for managing venue availability
- Implement endpoints for viewing venue calendar (GET /api/venues/{id}/calendar)

**Acceptance Criteria:**

- Users can view venue availability on a calendar

**Estimated Time:** 1 week

## Week 6-8: Booking Management

### US8: Implement Booking System

**Tasks:**

- Create Booking Entity and BookingRepository
- Implement BookingService with `bookVenue()` and `cancelBooking()` methods
- Implement endpoints for booking and canceling venues (POST/DELETE /api/bookings)

**Acceptance Criteria:**

- Users can book and cancel venue bookings

**Estimated Time:** 3 weeks

### US9: Implement Payment System

**Tasks:**

- Create Payment Entity and PaymentRepository
- Implement PaymentService with `processPayment()` method
- Implement endpoints for making payments (POST /api/payments)

**Acceptance Criteria:**

- Users can make payments for bookings

**Estimated Time:** 2 weeks

## Week 9-10: Review and Rating

### US10: Implement Review and Rating System

**Tasks:**

- Create Review Entity and ReviewRepository
- Implement ReviewService with `addReview()` and `getReviews()` methods
