"""
TensorFlow and agents compatibility patch to handle deprecated tf.contrib.distributions import
and missing function_tool from agents package.
This module should be imported before any modules that use tf.contrib.distributions or function_tool.
"""
import sys

# Handle TensorFlow import with graceful fallback
try:
    import tensorflow as tf

    # Check if tensorflow-probability is available
    try:
        import tensorflow_probability as tfp

        # Create a compatibility layer for tf.contrib.distributions
        if not hasattr(tf, 'contrib'):
            class ContribModule:
                pass
            tf.contrib = ContribModule()

        if not hasattr(tf.contrib, 'distributions'):
            tf.contrib.distributions = tfp.distributions

    except ImportError as e:
        # If tensorflow-probability is not available, create a more complete mock
        # This is a fallback that at least provides the basic structure
        import warnings
        warnings.warn(f"tensorflow-probability not found, using compatibility mock: {e}")

        if not hasattr(tf, 'contrib'):
            class ContribModule:
                pass
            tf.contrib = ContribModule()

        # Create a more complete mock for distributions that provides common classes and functions
        class MockDistributions:
            # Common distribution classes that might be needed
            class Distribution:
                pass

            class Normal:
                pass

            class MultivariateNormalDiag:  # This was the missing attribute
                pass

            class CustomKLDiagNormal:  # This seems to be needed based on the error
                pass

            class Bernoulli:
                pass

            class Categorical:
                pass

            class Beta:
                pass

            class Dirichlet:
                pass

            class Exponential:
                pass

            class Gamma:
                pass

            class Laplace:
                pass

            class StudentT:
                pass

            class Uniform:
                pass

            # Add required functions like RegisterKL
            @staticmethod
            def RegisterKL(dist1, dist2):
                # Mock implementation for RegisterKL function
                def decorator(func):
                    return func
                return decorator

            # Add other potentially needed functions
            @staticmethod
            def kl_divergence(dist1, dist2):
                # Mock implementation
                pass

        tf.contrib.distributions = MockDistributions

except ImportError as e:
    # If tensorflow itself is not available (e.g., DLL issues on Windows), create a minimal mock
    import warnings
    warnings.warn(f"TensorFlow not available, using compatibility mock: {e}")

    # Create a mock tf module to prevent import errors
    class MockTF:
        pass

    tf = MockTF()

    # Create a mock contrib module
    class ContribModule:
        pass

    tf.contrib = ContribModule()

    # Create a mock distributions module
    class MockDistributions:
        # Common distribution classes that might be needed
        class Distribution:
            pass

        class Normal:
            pass

        class MultivariateNormalDiag:  # This was the missing attribute
            pass

        class CustomKLDiagNormal:
            pass

        class Bernoulli:
            pass

        class Categorical:
            pass

        class Beta:
            pass

        class Dirichlet:
            pass

        class Exponential:
            pass

        class Gamma:
            pass

        class Laplace:
            pass

        class StudentT:
            pass

        class Uniform:
            pass

        # Add required functions like RegisterKL
        @staticmethod
        def RegisterKL(dist1, dist2):
            # Mock implementation for RegisterKL function
            def decorator(func):
                return func
            return decorator

        # Add other potentially needed functions
        @staticmethod
        def kl_divergence(dist1, dist2):
            # Mock implementation
            pass

    tf.contrib.distributions = MockDistributions

# Now handle the missing function_tool from agents package
# This might be needed if the agents package doesn't have the expected API
def function_tool(func):
    """
    Mock function_tool decorator for compatibility if not available in the installed agents package.
    """
    # Return the function as-is, since we're providing a compatibility layer
    return func

# Add this to the global namespace so it can be imported
sys.modules[__name__] = sys.modules[__name__]  # Ensure the module is properly referenced