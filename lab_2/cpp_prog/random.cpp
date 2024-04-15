#include <iostream>
#include <fstream>
#include "Consts.h"

int main() {
	try
	{
		srand(time(0));
		std::ofstream out;
		out.open(FILE_NAME);
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
	catch (const std::exception& err)
	{
		std::cout << err.what() << std::endl;
	}
}