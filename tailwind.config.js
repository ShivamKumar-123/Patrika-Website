    module.exports = {
        theme: {
        extend: {
            keyframes: {
            slideDown: {
                '0%': { transform: 'translateY(-100%)', opacity: '0' },
                '100%': { transform: 'translateY(0)', opacity: '1' },
            },
            fadeUp: {
                '0%': { transform: 'translateY(40px)', opacity: '0' },
                '100%': { transform: 'translateY(0)', opacity: '1' },
            },
            },
            animation: {
            slideDown: 'slideDown 0.8s ease-out',
            fadeUp: 'fadeUp 1s ease-out',
            },
        },
        },
    }
    