#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <limits>

std::vector<std::string> split(const std::string& str, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(str);
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

std::string bestPlanet(const std::vector<std::string>& solarSystem, int maxSize) {
    std::vector<std::string> requiredElements = {"H", "C", "N", "O", "P", "Ca"};
    std::string maxPlanet = "";
    int maxArea = std::numeric_limits<int>::min();

    for (const std::string& planet : solarSystem) {
        std::vector<std::string> planetData = split(planet, '_');
        std::string elements = planetData[0];
        int area = std::stoi(planetData[1]);

        std::vector<std::string> combinedElements;
        std::string currentElement = "";

        for (char c : elements) {
            if (std::islower(c)) {
                currentElement += c;
            } else {
                if (!currentElement.empty()) {
                    combinedElements.push_back(currentElement);
                }
                currentElement = std::string(1, c);
            }
        }

        if (!currentElement.empty()) {
            combinedElements.push_back(currentElement);
        }

        bool containsAllElements = std::all_of(requiredElements.begin(), requiredElements.end(),
            [&combinedElements](const std::string& element) {
                return std::find(combinedElements.begin(), combinedElements.end(), element) != combinedElements.end();
            });

        if (containsAllElements && area <= maxSize && area > maxArea) {
            maxPlanet = planet;
            maxArea = area;
        }
    }

    return maxPlanet;
}

int main() {
    std::vector<std::string> planets = {"OHNCCaP_100", "OHC_200", "OCa_50", "OHCCaP_400", "OHNCCaP_225", "OHCa_250"};
    int maxSize = 263;

    std::string result = bestPlanet(planets, maxSize);
    std::cout << result << std::endl;

    return 0;
}
