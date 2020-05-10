#!/bin/bash

# Create a doctor
curl -XPOST -H 'Content-Type: application/json' -d '{"name":"Jane Doe"}' http://localhost:3000/doctors

# Add a review to existing doctor
curl -XPOST -H 'Content-Type: application/json' -d '{ "description": "Jane Doe is a great doctor. Review 1"}' http://localhost:3000/doctors/1/reviews

# Add another review
curl -XPOST -H 'Content-Type: application/json' -d '{ "description": "Jane Doe is really a great doctor. Review 2"}' http://localhost:3000/doctors/1/reviews

# List all doctors and their reviews
curl -XGET -H 'Content-Type: application/json' http://localhost:3000/doctors

# List a doctor and the review(s)
curl -XGET -H 'Content-Type: application/json' http://localhost:3000/doctors/1

# Delete a review from a doctor
curl -XDELETE -H 'Content-Type: application/json' http://localhost:3000/doctors/1/reviews/2

# Delete a doctor
curl -XDELETE -H 'Content-Type: application/json' http://localhost:3000/doctors/1

# curl -XPOST -H 'Content-Type: application/json' -d '{"name":"John Smith"}' http://localhost:3000/doctors
# curl -XPOST -H 'Content-Type: application/json' -d '{ "description": "John Smith is a great doctor. Review 1"}' http://localhost:3000/doctors/2/reviews


# curl -XPOST -H 'Content-Type: application/json' -d '{"name":"Anooj Doe"}' http://localhost:3000/doctors
# curl -XPOST -H 'Content-Type: application/json' -d '{ "description": "Anooje Doe is a great doctor. Review 1"}' http://localhost:3000/doctors/3/reviews
# curl -XPOST -H 'Content-Type: application/json' -d '{ "description": "Anooje Doe is a great doctor. Review 2"}' http://localhost:3000/doctors/3/reviews
# curl -XPOST -H 'Content-Type: application/json' -d '{ "description": "Anooje Doe is a great doctor. Review 3"}' http://localhost:3000/doctors/3/reviews


# curl -XPOST -H 'Content-Type: application/json' -d '{"name":"Shah Doe"}' http://localhost:3000/doctors
# curl -XPOST -H 'Content-Type: application/json' -d '{ "description": "Shah Doe is a great doctor. Review 1"}' http://localhost:3000/doctors/4/reviews
