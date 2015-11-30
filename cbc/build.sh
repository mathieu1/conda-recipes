./configure --prefix=$PREFIX \
        --with-blas="-L$PREFIX/lib/ -lopenblas" \
        --with-lapack="-L$PREFIX/lib/ -lopenblas" \
        --enable-coinutils-threads --enable-cbc-parallel
make install -j ${CPU_COUNT}
