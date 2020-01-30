#include <iostream>
#include <algorithm>
#include <random>

struct Agent
{
    int id{};
    int score{};
};

std::vector<Agent> roulette_wheel(std::vector<Agent> const &agents)
{
    std::vector<int> scores;

    std::transform(agents.cbegin(),
                   agents.cend(),
                   std::back_inserter(scores),
                   [](Agent const &a) { return a.score; });

    std::vector<int> part_sums;

    std::partial_sum(scores.cbegin(),
                     scores.cend(),
                     std::back_inserter(part_sums));

    std::random_device rd;
    std::mt19937 eng(rd());
    std::uniform_int_distribution<> distr(0, part_sums.back() - 1);

    std::vector<Agent> results;

    std::generate_n(std::back_inserter(results), agents.size(),
                    [&]()
                    {
                        const auto iter = std::upper_bound(part_sums.cbegin(),
                                                           part_sums.cend(),
                                                           distr(eng));

                        return agents[std::distance(part_sums.cbegin(), iter)];
                    });

    return results;
}

int main()
{
    std::vector<Agent> const test_agents =
        {
            {0, 2},
            {1, 10},
            {2, 30},
            {3, 8},
            {4, 4}
        };

    for (auto const &agent : roulette_wheel(test_agents))
    {
        std::cout << "ID: " << agent.id << 
                     ", Score: " << agent.score 
                     << std::endl;
    }
}
