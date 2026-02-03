## Bucket 1

### Automated Territorial Defense / Pixel Warfare

#### Human description:

Certain regions of the canvas experienced extreme pixel placement in a specific pixel, with some individual pixels being repainted over 90,000 times. This level of sustained, repetitive activity far exceeds normal human interaction patterns and suggests the use of automated tools or scripts to defend some type of territory.

Evidence found that the irregular activity could exist:

- Table of top pixels

|   x |   y |   edits |
|----:|----:|--------:|
|   0 |   0 |   98807 |
| 359 | 564 |   69198 |
| 349 | 564 |   55230 |
| 859 | 766 |   52261 |
| 860 | 766 |   51485 |

- Table contains pixels with >50,000 edits

- Top users contributing hundreds of edits to the same tiny set of pixels (table evidence):

|     user_id |   edits_on_hot_pixels |
|------------:|----------------------:|
| 5.93665e+18 |                   653 |
| 1.99475e+17 |                   570 |
| 1.10989e+19 |                   554 |
| 1.60994e+18 |                   534 |
| 1.3479e+19  |                   533 |

#### Time Between Placement Exploration Evidence:

The time between placement distribution for users heavily involved in heavily contested pixels shows a sharp spike at a consistent interval, corresponding closely to the platform’s cooldown period. Unlike the broad, irregular timing expected from human interaction, this pattern suggests scripted or tool-assisted placement synchronized with the cooldown timer.

![Time Between Placements for Contested-Pixel Users](images/time_between_placements.png)

#### Session Length Exploration Evidence

This graph shows many of the users responsible for the highest placed pixels remained continuously active for sessions lasting 10–25 hours without breaks longer than 30 minutes. This type of sustained activity is inconsistent with normal human usage patterns and suggests automated or tool-assisted behavior as people live lives still and need sleep. Comparing this to a baseline graph of the session length for all r/place users it is clear the session lengths are much higher for the users in the top contestested pixel areas than general users.

**Session lengths for heavily contested-pixel users:**

![Session Lengths for Contested-Pixel Users](images/session_lengths_top_users.png)

**Session lengths across all r/place users:**

![Session Lengths for All Users](images/session_lengths_overall.png)

#### Spatial Concentration Exploration Evidence

Looking at edit concentration shows that while many users placed pixels across a wide range of locations, a subset of the users in the high pixel placement areas directed a majority of their activity toward a very small set of heavily contested pixels. In several cases, more than half and sometimes nearly all of a user’s placements occurred in these high placement area regions. This level of spatial focus is inconsistent with typical human participation patterns and suggests automated or tool-assisted territorial defense behavior trying to maintain a specific art work or control of a contested area.

![Fraction of Edits in Hot Pixels](images/hot_edit_ratio.png)

#### Conclusion

Taken together, these behavioral patterns: 

extreme pixel churn, cooldown-synchronized timing, unusually long continuous activity sessions, and highly concentrated spatial focus 

all form a consistent profile of automated or tool-assisted territorial defense rather than typical human participation.


## Bucket 2  

### Low Color Diversity / Task-Specialized Automation

#### Human description:

A subset of highly active accounts exhibited extremely low color diversity, placing hundreds of pixels while using only one or two colors. Unlike typical participants who switch colors while contributing to artwork, these accounts repeatedly placed the same color in highly localized areas. This pattern suggests task-focused, repetitive behavior consistent with automated scripts or tool-assisted placement rather than normal human artistic participation.

Evidence found that the irregular activity could exist:

- Distribution of color diversity ratios per user  
- Table of highly active users with only 1–2 total colors used  
- Per-user spatial maps showing tightly localized placement patterns  

#### Color Diversity Exploration Evidence:

Analysis of per-user color usage shows that several accounts made between 200 and 700 placements while using only one or two colors. These users have color diversity ratios below 0.01, meaning over 99% of their placements were the same color. Human contributors typically use a broader range of colors when creating or modifying artwork, making this extreme level of repetition highly unusual.

#### Color Dominance Exploration Evidence

Further analysis of dominant color usage reveals that many of these accounts placed nearly all of their pixels using a single color. In several cases, more than 98–100% of a user’s placements were the same color. Such extreme color specialization is consistent with automated or tool-assisted behavior focused on repetitive maintenance tasks, such as border reinforcement or template correction.

#### Spatial Pattern Exploration Evidence

Visual inspection of the most extreme low-entropy users shows highly localized placement patterns. Each account concentrated its activity in small clusters or narrow boundary regions rather than contributing broadly across the canvas. Some users appear to maintain straight edges or repeatedly correct the same limited set of pixels. This spatial behavior aligns with automated maintenance roles rather than creative human participation.

![Pixel Placement Patterns of Top Low Color Diversity Users](images/low_entropy_user_patterns.png)

*Figure: Spatial placement patterns for the five most extreme low color-diversity users. Each panel shows that activity is concentrated in small, highly localized regions rather than spread across broader artwork, consistent with task-focused automated or tool-assisted maintenance behavior.*

#### Conclusion

Taken together, these behavioral patterns:

extremely low color diversity, overwhelming dominance of a single color, and tightly localized spatial placement patterns

form a consistent profile of task-specialized, repetitive behavior. These signals strongly suggest automated or tool-assisted accounts performing targeted maintenance functions rather than typical human artistic contribution.


| user_id              | total_colors | total_edits | color_diversity_ratio |
|----------------------|--------------|-------------|------------------------|
| 13973723605168343779  | 1            | 406         | 0.002463               |
| 1357144649154069865   | 1            | 403         | 0.002481               |
| 8684514774390412613   | 1            | 396         | 0.002525               |
| 14155905291761609074  | 2            | 692         | 0.002890               |
| 3949342267876374367   | 1            | 334         | 0.002994               |



## Bucket 3 

### Mass First-Time User Onboarding Spike

#### Human description:

During several short time windows, the platform experienced unusually large surges of first-time participants placing their very first pixel. These spikes represent moments where thousands of new accounts became active almost simultaneously. While high activity is expected during major events, the scale and sharpness of these onboarding bursts suggest organized influxes of users rather than gradual organic growth.

Evidence found that the irregular activity could exist:

- Minute-level placement activity time series showing sharp spikes  
- Table of first-time user counts per minute  
- Z-score analysis comparing spike minutes to the overall average  

#### First-Time User Spike Exploration Evidence:

Analysis of the timestamp of each user’s first placement reveals distinct minutes where new-user activity far exceeded normal levels. In one case, nearly 6,000 accounts placed their first-ever pixel within a single minute, compared to an average of roughly 2,000 new users per minute across the dataset. This spike produced a Z-score greater than 4, indicating the surge is statistically extreme relative to baseline behavior.

#### User Lifespan Exploration Evidence

Further examination of these first-time users shows that many remained active well beyond their initial placement. A substantial portion continued placing pixels for hours, and in some cases more than a day, suggesting that these accounts were not simply testing the system but were participating in sustained activity. This pattern is consistent with coordinated onboarding tied to specific community efforts or organized participation waves.

#### Temporal Concentration Exploration Evidence

The onboarding surges occurred in narrow, sharply defined time windows rather than gradually over longer periods. The rapid rise and fall in first-time user counts suggests synchronized participation driven by external coordination, such as social media mobilization, livestream events, or community calls to action.

#### Conclusion

Taken together, these behavioral patterns:

statistically extreme spikes in first-time users, sustained post-onboarding activity, and tightly concentrated timing windows

indicate coordinated waves of new participants joining the canvas. While not necessarily automated, this activity represents irregular participation dynamics driven by organized or highly synchronized community engagement rather than steady organic growth.
