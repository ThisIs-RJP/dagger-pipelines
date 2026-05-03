import dagger
from dagger import dag, function, object_type


@object_type
class DaggerPipelines:
    @function
    async def echo_context(
        self,
        repo_name: str,
        branch: str,
    ) -> str:
        return await (
            dag.container()
            .from_("alpine:3.20")
            .with_exec(["echo", f"repo={repo_name} branch={branch}"])
            .stdout()
        )
