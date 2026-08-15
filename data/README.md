# Data

## Dataset

This project uses behavioral data from the Dual Mechanisms of Cognitive Control (DMCC55B) dataset.

## Source

OpenNeuro Dataset: ds003465

The dataset was created by researchers at Washington University in St. Louis and accompanies a peer-reviewed publication in Scientific Data.

## Task

This project focuses on the Stroop cognitive-control task.

Participants completed different Stroop conditions. Reaction time and response accuracy will be analyzed to investigate the behavioral effects of cognitive conflict.
## Results

### Reaction Time

Mean reaction time was:

- Congruent trials: 0.717 seconds
- Incongruent trials: 0.736 seconds

The Stroop interference effect was approximately **0.019 seconds (18.97 ms)**, indicating that responses were slower during incongruent trials.

![Mean Reaction Time by Stroop Trial Type](figures/stroop_reaction_time.png)

### Accuracy

Mean response accuracy was:

- Congruent trials: 100%
- Incongruent trials: 97.2%

Accuracy was slightly lower during incongruent trials, consistent with increased cognitive conflict.

![Mean Accuracy by Stroop Trial Type](figures/stroop_accuracy.png)

## Why this dataset is trustworthy

DMCC55B is a publicly available research dataset hosted on OpenNeuro and documented in a peer-reviewed scientific publication.
## Interpretation

The results demonstrate a Stroop interference effect. Participants responded more slowly to incongruent trials than to congruent trials, with an average reaction-time difference of approximately 18.97 ms.

Accuracy was also slightly lower for incongruent trials (97.2%) compared with congruent trials (100%).

Together, these findings are consistent with the cognitive conflict produced by incongruent Stroop stimuli, where competing information increases the demands on cognitive control.