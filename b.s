	.arch armv8-a
	.text
	.align	2
	.global	main
	.type	main, %function
main:
    mov x0, 0
    movk x0, ${outer}, LSL 16
.loop_inner_init:
    ${nop}
    mov x1, ${inner}
.loop_inner:
    sub x1, x1, 1
    cbnz x1, .loop_inner
.loop_outer:
    sub x0, x0, 1
    cbnz x0, .loop_inner_init
    ret
	.size	main, .-main
