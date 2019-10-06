# NC Voter Records for 2016 & 2018
This set contains various datasets regarding election results either by county, zip, or precinct for both the general and primary elections. Your job is to find intertwining connections between the data to give it meaning!

# Important Variable Definitions

**Contest related attributes**

-   election_date
-   contest_group_id: an identifier to link a contest across multiple counties
-   contest_name
-   contest_type: state or county
-   is_partisan: whether the election is partisan or not
-   has_primary: whether a candidate for a particular contest first must compete in a primary before running in a general election. For partisan races, this value will be true if the number of candidates in a particular party in a particular a contest is greater than the value in the vote_for field (the number of seats that are up for election). If candidates > seats for a given party, then the board of elections will actually hold a primary, print ballots, etc. If candidates <= seats for a given party, then the board of elections will not bother with holding a primary, etc., since the result is a foregone conclusion. For non-partisan races (some of which still have primaries) this value will be true only if the number of candidates in any party exceeds the number of seats up for grabs. As this field exists in the candidate listing CSV found in #7, the value of TRUE only indicates the relationship between the number of candidates and the open seats. At least in this CSV, the field is not an indicator of whether rules for a contest require a primary. For example, if there is only one Republican candidate in a single-seat contest for which rules require a partisan primary then the value of has_primary would be FALSE.
-   party_contest: is null unless both has_primary and is_partisan are TRUE. The values of party_contest should be DEM, REP or LIB.
-   vote_for
-   term
-   is_unexpired: whether an contest is being held before the normal expiration of the previous incumbent's term.
County related attributes
-   district
-   county

**Precinct related attributes**

-   precinct: note that this column has vote type in it, such as ABSENTEE, ONE STOP 100, PROVISIONAL.

**Candidate related attributes**

-   candidate
-   first_name
-   middle_name
-   last_name
-   name_suffix_lbl
-   nick_name
-   party_candidate: party affiliation of a candidate
-   candidacy_date
-   election_day: number of votes received at the election day
-   one_stop: number of one-stop votes
-   absentee_by_mail: number of absentee-by-mail votes
-   provisional: number of provisional votes
-   total_votes: total number of votes
-   winner_flag: whether winner of the contest

# Additional Information
Each of the provided datasets provides the results of each contents in various geographic areas in either 2016 or 2018, by either state, precinct, or county
 
