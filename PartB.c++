#include <iostream>
using namespace std;

int main() {
    double sum = 0.0;  // To store the sum of the series

    // Loop through the series
    for (int numerator = 1, denominator = 3; numerator <= 95; numerator += 2, denominator += 2) {
        sum += static_cast<double>(numerator) / denominator;
    }

    // Output the sum
    cout << "Sum of the series: " << sum << endl;

    return 0;
}
