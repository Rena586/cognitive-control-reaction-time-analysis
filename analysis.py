import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data/sub-f1027ao_ses-wave1bas_task-Stroop_acq-mb4AP_run-1_events.tsv", sep="\t")
print(data.head())
print("\nColumn names:")
print(data.columns.tolist())
print("\nTrial types:")
print(data["trial_type"].value_counts())
print("\nMean reaction time by trial type:")
print(data.groupby("trial_type")["response_time"].mean())
print("\nMean accuracy by trial type:")
print(data.groupby("trial_type")["response_accuracy"].mean())
con_rt = data[data["trial_type"] == "Con"]["response_time"].mean()
incon_rt = data[data["trial_type"] == "InCon"]["response_time"].mean()

stroop_effect = incon_rt - con_rt

print("\nStroop interference effect:")
print(stroop_effect)
# Create a bar chart of mean reaction time by trial type
mean_rt = data.groupby("trial_type")["response_time"].mean()

mean_rt.plot(kind="bar")

plt.title("Mean Reaction Time by Stroop Trial Type")
plt.xlabel("Trial Type")
plt.ylabel("Mean Reaction Time (seconds)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("figures/stroop_reaction_time.png", dpi=300)
plt.show()
# Create a bar chart of mean accuracy by trial type
mean_accuracy = data.groupby("trial_type")["response_accuracy"].mean()

mean_accuracy.plot(kind="bar")

plt.title("Mean Accuracy by Stroop Trial Type")
plt.xlabel("Trial Type")
plt.ylabel("Mean Accuracy")
plt.xticks(rotation=0)
plt.ylim(0, 1.05)
plt.tight_layout()
plt.savefig("figures/stroop_accuracy.png", dpi=300)
plt.show()