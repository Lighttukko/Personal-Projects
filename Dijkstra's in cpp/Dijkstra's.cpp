#include <iostream>

class Graph{
    public:
        char *letters;
        int **matrix;
        int total;

        Graph(int total){
            this->total = total;
            this->letters = new char[total];
            this->matrix = new int*[total];
            for (int x = 0; x < total; ++x){
                this->matrix[x] = new int[total];
            }

            for (int x = 0; x < total; ++x){
                for (int y = 0; y < total; ++y){
                    this->matrix[x][y] = 0;
                }
            }
        }

        int finder(char letter){
            for (int x = 0; x < this->total; ++x){
                if (this->letters[x] == letter){
                    return x;
                }
            }
            return -1;
        }

        void add_data(int position, char letter){
            if (position < this->total && position >= 0){
                for (int x = 0 ; x < this->total; ++x){
                    if (this->letters[x] == letter){
                        return;
                    }
                }
                this->letters[position] = letter;
            }
            
        }

        void add_connection(int letter1, int letter2, int weight){
            if (letter1 >= 0 && letter1 < this->total && letter2 >= 0 && letter2 < this->total && weight > 0){
                this->matrix[letter1][letter2] = weight;
                // this->matrix[letter2][letter1] = weight;
            }
        }

        void printer(){
            std::cout << "graph" << std::endl;
            for (int x = 0; x < this->total; ++x){
                std::cout << this->letters[x] << ": ";
                for (int y = 0; y < this->total; ++y){
                    std::cout << this->matrix[x][y] << " ";
                }
                std::cout << std::endl;
            }
        }

        int** dijkstra(char letter1){
            int letter = -1;
            int *distances = new int[this->total];
            int *path = new int[this->total];
            bool visited[this->total];
            for (int x = 0; x < this->total; ++x){
                distances[x] = 0;
                path[x] = -1;
                visited[x] = false;
                if (this->letters[x] == letter1){
                    letter = x;
                }
            }
            if (letter == -1){
                return nullptr;
            }
            int queue[this->total], q_start = 0, q_end = 0;
            queue[q_end++] = letter;
            while(q_end > q_start){
                int start = queue[q_start++];
                visited[start] = true;
                for (int x = 0; x < this->total; ++x){
                    if (this->matrix[start][x] > 0 && !visited[x]){
                        queue[q_end++] = x;
                        if (distances[x] == 0 || distances[x] > (this->matrix[start][x] + distances[start])){
                            distances[x] = this->matrix[start][x] + distances[start];
                            path[x] = start;
                        }
                    }
                }
            }
            int** leo = new int*[2];
            leo[0] = distances;
            leo[1] = path;
            return leo;
        }
    char* get_path(char start, char end) {
        int s = finder(start);
        int e = finder(end);
        if (s == -1 || e == -1) {
            return nullptr;
        }

        int* path = dijkstra(start)[1];
        if (!path) {
            return nullptr;
        }

        int tempPath[this->total];
        int count = 0;
        for (int v = e; v != -1; v = path[v]) {
            tempPath[count++] = v;
            if (v == s) break;
        }

        char *finalPath = new char[count + 1];
        for (int i = 0; i < count; ++i) {
            finalPath[i] = this->letters[tempPath[count - i - 1]];
        }
        finalPath[count] = '\0';

        delete[] path;
        return finalPath;
    }


        // char* get_path(char start, char end){
        //     int paths[this->total];
        //     int s = finder(start);
        //     int e = finder(end);
        //     int *path = dijkstra(start)[1];
        //     int x = 0;
        //     paths[x] = path[e];
        //     x += 1;
        //     for (; x < this->total; ++x){
        //         paths[x] = path[paths[x - 1]]; //1, 2, 0
        //         if (paths[x] == s){
        //             ++x;
        //             break;
        //         }
        //     }//x = 3
        //     char *leo = new char[x + 1];
        //     for (int y = x; y > 0; --y){
        //         leo[x-y-1] = this->letters[paths[y]];
        //     }
        //     return leo;

        // }

};

int main(){
    Graph g(7);
    g.add_data(0, 'A');
    g.add_data(1, 'B');
    g.add_data(2, 'C');
    g.add_data(3, 'D');
    g.add_data(4, 'E');
    g.add_data(5, 'F');
    g.add_data(6, 'G');

    g.add_connection(3, 0, 4); // D - A, weight 4
    g.add_connection(3, 4, 2); // D - E, weight 2
    g.add_connection(0, 2, 3); // A - C, weight 3
    g.add_connection(0, 4, 4); // A - E, weight 4
    g.add_connection(4, 2, 4); // E - C, weight 4
    g.add_connection(4, 6, 5); // E - G, weight 5
    g.add_connection(2, 5, 5); // C - F, weight 5
    g.add_connection(2, 1, 2); // C - B, weight 2
    g.add_connection(1, 5, 2); // B - F, weight 2
    g.add_connection(6, 5, 5); // G - F, weight 5
    g.printer();
    int **d = g.dijkstra('A');
    for (int x = 0; x < 7; ++x){
        std::cout << d[0][x] << ", ";

    }
    std::cout << std::endl;
    for (int x = 0; x < 7; ++x){
        std::cout << d[1][x] << ", ";

    }
    std::cout << std::endl;
    char *lin = g.get_path('A', 'F');
    int size = sizeof(lin)/sizeof(char);
    for (int x = 0; x < size; ++x){
        std::cout << lin[x];
    }

    delete[] d[0];
    delete[] d[1];
    delete[] d;
    return 0;
}