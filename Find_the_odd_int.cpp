#include <iostream>
#include <unordered_map>
#include <vector>

int find_it(const std::vector<int>& seq) {
    std::unordered_map<int, int> element_count;
    
    // Преброяване на срещанията на всеки елемент в масива
    for (int element : seq) {
        if (element_count.find(element) != element_count.end()) {
            element_count[element] += 1;
        } else {
            element_count[element] = 1;
        }
    }
    
    // Намиране на елемента с нечетен брой срещания
    for (const auto& pair : element_count) {
        if (pair.second % 2 != 0) {
            return pair.first;
        }
    }
    
    return -1;
}

int main() {
    std::vector<int> seq = {1, 2, 3, 2, 1, 3, 1};
    int result = find_it(seq);
    std::cout << result << std::endl;
    
    return 0;
}
