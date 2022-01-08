# Hotspot

 Create a Business User (Demographic best associated with them needs to be chosen) (Needs to be updated based on deals going on each day)
 - Create a Consumer User (Demographic preferences need to be chosen) (18+, 21+ - Businesses would choose which they would be allowed to take)
 - Generate an list of recommendations for Consumer (Needs to continue to update for Consumer based on choices)
 - Keep track of Business's Quota for how many people they want for the night
 - Send Quota Amount of "Invites" to Users depending if they fit that Business's Preferences
 - Keep track of Users choices ("Like" Businesses they want, so they can access favorite clubs)
 - Allow Consumers to Accept or Deny Invites
 - Retrieve User's Location -> (Map to help visualize distance)
 - Keep track if user has visited location (Review based on Thumbs up or down)

 CRUD: Create - Read - Update - Delete. How can the users transform the data your API accesses?
     - Have 2 separate  "Create" functions, one for each type of user.
     - Read through both user types to create recommendations for Comsumers, and invites to give on night of for businesses
     - Update Business Quotas depending on number of invites that were invited - based on given demographics
     - Update Consumer recommendations depending on their "Likes" of Businesses
     - Delete: each type of User can delete their profiles

 ## Design

 - Use flask_restx to build an API server
 - Multiple clients possible -- TBD
 - Handle each major requirement with an API endpoint
 - Use Test-Driven-Development (TDD) to make sure we have testing.
 - Use Swagger for initial interaction with server.
 - Use Swagger, pydoc and good docstrings for documentation.
 - Endpoints:
 -   Create a business user with `/create_buser` endpoint. Inputs: Name, Hours, Location,Club type, Pictures, Age restrictions, Quota, Demographic they want, 
 -   Create a consumer user with '/create_cuser' endpoint. Inputs: Name, Age, Demographics, Initial Club Interest Categories, Location
 -   Create an RSVP with '/create_invite' endpoint. Inputs: Business Name, Location, Time of, Number of +1s
 -   Take input from Consumer and "sending" response to business with '/invite_response' endpoint. Inputs: Accept or Deny, Number of Additional People
 -   Keep track of Consumer preferences with '/rec_response' endpoint. Inputs: Thumbs Up or Thumbs Down
 -   Generate list of recommendations with '/rec_list' endpoint. Inputs: Consumer preferences, Business demographic, Consumer demographic
 -   Reset list of recommendations with 'reset_list' endpoint. Resets at 4:00 am.
