# PrimeCipher  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  

# PrimeCipher-Decoding-Primes-in-Binary-Strings
A high-performance Python tool that efficiently extracts unique prime numbers concealed within binary data. Powered by mathematical optimizations and algorithmic analysis for minimum time complexity (Big O) and maximum speed.

## ✨ Key Features

⚡  Cache-Optimized Primes** - Advanced cached prime detection for blazing speed  
📊 Big O Analyzed** - Detailed time/space complexity breakdowns  
🔢 Efficient Binary Processing** - Handles large inputs with minimal memory  
📈 Benchmark Ready** - Compare optimization strategies via runtime tests  

## ⚡ Performance Analysis

| Operation             | Time Complexity     | Space Complexity |
|-----------------------|---------------------|------------------|
| Binary Validation     | O(n)                | O(1)             |
| Prime Checking        | O(√n)               | O(1)             |
| Substring Generation  | O(n²)               | O(n)             |
| **Overall**           | O(n² * √m)          | O(k)             |

> Where:  
> - `n` = length of the binary string  
> - `m` = maximum value of a substring  
> - `k` = number of unique primes found




## Example Input/Output

| Input        | Description   | Output                       | Running Time         |
|--------------|----------------|------------------------------|----------------------|
| `1011001`, N=`50` | Binary string with range limit | `5: 2, 3, 5, 11, 13`  | `0.000423 seconds`   |




## 📊 Optimization Opportunities

| Optimization        | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Prime Checking       | Upgrade to **Miller-Rabin test** for probabilistic primality (~O(k log³n)) |
| Memoization          | **Cache** previously checked numbers to avoid redundant checks             |
| Early Termination    | **Skip** substrings longer than `log₂N` bits for efficiency                |
| Parallel Processing  | **Process substrings concurrently** to leverage multi-core performance     |


## 🌐 Potential Applications

- 🔐 Cryptography key generation  
- 📊 Number theory research  
- 🏆 Competitive programming challenges  
- 🧮 Binary data analysis



## 💡 Why This Stands Out

- 🧱 **Clean Architecture**: Separated validation, processing, and output
- 🤝 **User-Friendly**: Interactive console input with error handling
- 🔬 **Research-Ready**: Built-in timing for algorithm analysis
- 📈 **Scalable**: Handles arbitrarily long binary strings



## 🔜 Future Enhancements

- 🧪 Add Miller-Rabin primality test
- 💾 Implement memoization cache
- 🌐 Create web interface version
- 📂 Add batch processing from files


## 🛠️ Installation & Usage

```bash
# Clone the repository
git clone https://github.com/d4t4tect/PrimeCipher-Decoding-Primes-in-Binary-Strings.git

# Navigate to the project folder
cd PrimeCipher-Decoding-Primes-in-Binary-Strings

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies (none needed, but for structure)
pip install -r requirements.txt

# Run the script
python primecipher.py
