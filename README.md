# SampleAggregator
Service which aggregate samples into sessions

## Implementation Description
The aggregator service gets a sample as input and checks if earlier sample recieved from the same machine and from the same sampled hour (up to 15 min between the 2 samples).
Afterwards, it is seperated to 2 scenarios:
  * Infinite lag allowed:
    Wait until the second smaple arrived to cloud. once arrived, creating new sample.
  * Up to 2 hours lag:
    Wait up to 2 hours to get the second sample. In case that 2 hours have passed, ithe last sample is discarded.

Assumption for simplify - all the samples can be saved in memory.
* I would implement saving to file system according to machine_id saples after x (according to system scale requirements) samples arrived and every time that sample arrived, check if earlier sample is in memory and if not, search in the files that saved on file system.

![alt text](https://github.com/haimgil/SampleAggregator/blob/e0dd8e9812c0b511c0ba77ea012a4841baf76475/Flow%20chart.png)
