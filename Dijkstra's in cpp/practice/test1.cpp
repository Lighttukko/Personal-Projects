#include <iostream>

int main(){
    std::vector<int> nums;
    nums.push_back(10);
    nums.resize(3);
    std::cout << nums[0] << std::endl ;
    return 0;
}