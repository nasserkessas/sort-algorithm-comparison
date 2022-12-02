CC=g++
IDIR=.
CFLAGS=-I$(IDIR)

ODIR=bin
LDIR =bin

# LIBS=-lm

_DEPS = sort.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = bubble_sort.o  comb_sort.o  heap_sort.o  insertion_sort.o  selection_sort.o  shuffle.o  sort.o
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


$(ODIR)/%.o: %.cpp $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

sort: $(OBJ)
	$(CC) -o $(ODIR)/$@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*