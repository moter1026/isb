#include <iostream>
#include <fstream>


#define SUBSEQUENCE_LEN 128

int main() {
	srand(time(0));
	std::ofstream out;
	out.open("../../out_cpp.txt");
    if (out.is_open())
    {
		for (size_t i = 0; i < SUBSEQUENCE_LEN; ++i)
		{
			out << rand() % 2;
		}
    }
    out.close();
    std::cout << "File has been written" << std::endl;
	return 0;
}