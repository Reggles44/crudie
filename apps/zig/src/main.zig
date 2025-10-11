const std = @import("std");
const zig = @import("zig");
const zap = @import("zap");

fn healthcheck(r: zap.Request) !void {
    

}

fn not_found(req: zap.Request) !void {
    std.debug.print(req.path, )
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{.thread_safe=true}){};
    const allocator = gpa.allocator();
    
    var router = zap.Router.init(allocator, .{.not_found = })
    try simpleRouter.handle_func_unbound("/", healthcheck);
    try simpleRouter.handle_func_unbound("/create", healthcheck);
    try simpleRouter.handle_func_unbound("/", healthcheck);
    try simpleRouter.handle_func_unbound("/", healthcheck);
    try simpleRouter.handle_func_unbound("/", healthcheck);


    var listener = zap.HttpListener.init(.{
        .port = 3000,
        .on_request = router.on_request_handler(),
        .log = true,
        .max_clients = 100000,
    });

    std.debug.printf
        \\ Listening on 0.0.0.0:3000
        \\ 
        \\ Test me with:
        \\    curl http://localhost:8888/
        \\
        \\
    , .{});

    // start worker threads
    zap.start(.{
        .threads = 2,

        // Must be 1 if state is shared
        .workers = 1,
    });
}

