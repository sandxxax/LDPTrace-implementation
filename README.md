# LDPTrace-implementation

This repository implements the LDPTrace - a tool which helps with Local Differential Privacy for Trajectories.

This is the Python implementation for the paper: [LDPTrace](https://www.vldb.org/pvldb/vol16/p1897-gao.pdf)

> Yuntao Du, Yujia Hu, Zhikun Zhang, Ziquan Fang, Lu Chen, Baihua Zheng and Yunjun Gao (2023). LDPTrace: Locally Differentially Private Trajectory Synthesis.  Paper in [arXiv](https://arxiv.org/abs/2302.06180) or [PVLDB](https://www.vldb.org/pvldb/vol16/p1897-gao.pdf). In VLDB'23, Vancouver, Canada, August 28 to September 1, 2023.

> See the official notes by the authors [blog](https://research.zealscott.com/blog/2023/04/22/LDPTrace/) for the introduction to this work.


## 1. Environment Requirements

- Ubuntu OS
- Python >= 3.8 (Anaconda3 is recommended)
- numpy == 1.21.4


## 2. Dataset

### I. Dataset Statistics

The experiment was conducted on the oldenberg trajectory datasets. The overall statistics are listed below:

| Dataset   | Size      | Average Length | Sampling Interval |
| --------- | --------- | -------------- | ----------------- |
| Oldenburg | 104   | 9.91         | 0.200 sec          |


Oldenburg dataset is provided for testing.

### II. Oldenburg

* Oldenburg is a synthetic dataset simulated by Brinkhoff's network-based moving objects generator. It is based on the map of Oldenburg city, Germany.

* For Oldenburg dataset, please refer to http://iapg.jade-hs.de/personen/brinkhoff/generator/ to generate the synthesized dataset. The setting parameters used as per the official paper are as follows:
   * obj./time 0 0
   * maximum time: 1000
   * classes: 1 0
   * max. speed div: 50

* After obtaining the raw dataset, it needs to be transformed to the standard input format:

   ```
   #0:
   >0: x_0,y_0; x_1,y_1;...
   #1:
   >0: x_0,y_0; x_1,y_1;...
   #2:
   >0: x_0,y_0; x_1,y_1;...
   >0: x_0,y_0; x_1,y_1;...
   >0: x_0,y_0; x_1,y_1;...
   #3: 
   >0: x_0,y_0; x_1,y_1;...
   >0: x_0,y_0; x_1,y_1;...
   #4: 
   >0: x_0,y_0; x_1,y_1;...
      
   ...
   ```
   '>0' is a fixed string denoting the start of a trajectory.

  We have added a function in the `./LDPTrace/code/`  folder called, transformdataset.py for transforming the .dat into the required format specified above for the implementatiom.

  If, the dataset is not in the above format, You can run the fuction after modifying the dataset file path to obtain the dataset with proper format.
  
* The Generator by http://iapg.jade-hs.de/personen/brinkhoff/generator/ couldnt help us with the creation of dataset, as it was throwing in some errors.

  You can clone the official repo for the Generator using this link : https://github.com/kwnam4u/brinkhoff
  
* We used another repo for obtaining the dataset used for the experimentation.

  The link to that repo is : https://github.com/nichujie/brinkhoff
  We used the output file containing the oldenberg.dat file for the experimentation and implementation.
  
* Always locate the dataset into `./LDPTrace/data/` dictionary.


##  3. Implementation and Reproducing the results

Please make sure the data file is in ``./LDPTrace/data/`` dictionary, and its in .dat format, and also its in the above specified format!

Here's an example of running LDPTrace:

With the below command, you are running the main function with a few arguements. 

NOTE: --re_syn must be given, if dataset is not pre-configured already.!
```python
python main.py --dataset oldenburg --grid_num 6 --epsilon 1.0 --re_syn --multiprocessing
```
or, you can also try the following command, as oldenburg is the default dataset for the main function.!
```python
python main.py
```

LDPTrace will save the synthesized database in ``./LDPTrace/data/DATASET_NAME/`` and output the Evaluation/Experiment metrics.

## 4. Configurations

The running parameters include:

+ --dataset: 
  + 'oldenburg': for Oldenburg dataset
+ --epsilon: privacy budget
+ --grid_num: grid granularity `N`, the spatial map will be decomposed into `N x N` grids. Based on the theoretical analysis in our paper, we recommend `N=6` for Oldenburg, Porto and Campus dataset.
+ --max_len: quantile of estimated max length, the default setting is 0.9
+ --size_factor: reciprocal of query size `r` (i.e., `1/r`), the default setting is 9
+ --query_num: the number of range queries, LDPTrace will output the average query error. The default setting is 200
+ --re_syn: whether to re-synthesize the database. If this parameter is not set, LDPTrace will try to read the saved databased that is synthesized before.
+ --multiprocessing: whether to use multiprocessing in experiments to improve efficiency.

## 5. Acknowledgement

Any scientific publications that use the datasets/codes of the above specified paper should cite the original paper as per the reference:

```
@inproceedings{LDPTrace,
  author    = {Yuntao Du and 
               Yujia Hu and 
               Zhikun Zhang and
               Ziquan Fang and 
               Lu Chen and 
               Baihua Zheng and 
               Yunjun Gao},
  title     = {{LDPTrace}: Locally Differentially Private Trajectory Synthesis},
  booktitle = {{PVLDB}},
  pages     = {1897--1909},
  year      = {2023}
}
```

## 6. Contributors :
  1. Sandhya V : contact me @[mail-me](vsandhya912@gmail.com) and [Github-link](https://github.com/sandxxax/)
  2. Arun Ashok Badri : contact me @[mail-me](iamarunbadri@gmail.com) and [Github-link](https://github.com/0hex7/)
  3. PavanKumar J : contact me @[mail-me](pavankumarj.cy@gmail.com) and [Github-link](https://github.com/lonelypheonix/)





