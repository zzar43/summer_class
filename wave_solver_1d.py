from src import *

def main():

    Nx = 401
    h = 1 / (Nx-1)

    my_mesh = Mesh1D(h, Nx)

    print(my_mesh)

    pass

if __name__ == "__main__":
    main()