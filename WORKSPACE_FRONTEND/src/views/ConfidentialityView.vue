<script setup>

import {
ShieldCheck,
Lock,
Building2,
Users,
Database,
CreditCard,
ArrowRight,
CheckCircle2,
XCircle,
Activity,
BadgeCheck,
MessageCircleMore
} from "lucide-vue-next"


</script>
<template>
<div>
<!-- HERO -->

<section class="py-6.5 bg-[#F7F8FA]">

    <div class="max-w-7xl mx-auto px-6">

        <div
            class="bg-white rounded-[40px] border border-[#E5E7EB] overflow-hidden shadow-sm">

            <div class="grid lg:grid-cols-2">

                <!-- LEFT -->

                <div class="p-14 flex flex-col justify-center">

                    <div
                        class="inline-flex items-center gap-3 w-fit px-5 py-2 rounded-full bg-[#F9A825]/10">

                        <ShieldCheck
                            class="w-5 h-5 text-[#F9A825]" />

                        <span
                            class="font-semibold text-[#F9A825]">

                            Security & Confidentiality

                        </span>

                    </div>

                    <h1
                        class="mt-8 text-5xl font-bold text-[#1F2937] leading-tight">

                        Protecting Your
                        Information
                        <span class="text-[#F9A825]">

                            Every Step
                            of the Way

                        </span>

                    </h1>

                    <p
                        class="mt-6 text-lg leading-8 text-[#374151] max-w-xl">

                        At WorkSpace, confidentiality is more than
                        a policy. We protect your personal data,
                        booking history, and business information
                        using modern security practices designed
                        to keep your information safe.

                    </p>

                    <div
                        class="flex gap-4 mt-10">

                        <RouterLink
                            to="/privacy-policy"
                            class="bg-[#F9A825] hover:bg-yellow-500 transition text-white px-7 py-4 rounded-xl font-semibold flex items-center gap-2">

                            Privacy Policy

                            <ArrowRight
                                class="w-5 h-5" />

                        </RouterLink>

                    </div>

                </div>

                <!-- RIGHT -->

                <div
                    class="bg-[#1F2937] flex items-center justify-center p-14">

                    <div
                        class="grid grid-cols-2 gap-6 w-full">

                        <div
                            class="bg-white/10 rounded-3xl p-8 backdrop-blur">

                            <ShieldCheck
                                class="w-10 h-10 text-[#F9A825]" />

                            <h3
                                class="mt-6 text-white font-semibold">

                                Secure Platform

                            </h3>

                        </div>

                        <div
                            class="bg-white/10 rounded-3xl p-8">

                            <Lock
                                class="w-10 h-10 text-[#F9A825]" />

                            <h3
                                class="mt-6 text-white font-semibold">

                                Encrypted Data

                            </h3>

                        </div>

                        <div
                            class="bg-white/10 rounded-3xl p-8">

                            <Database
                                class="w-10 h-10 text-[#F9A825]" />

                            <h3
                                class="mt-6 text-white font-semibold">

                                Protected Storage

                            </h3>

                        </div>

                        <div
                            class="bg-white/10 rounded-3xl p-8">

                            <Users
                                class="w-10 h-10 text-[#F9A825]" />

                            <h3
                                class="mt-6 text-white font-semibold">

                                Trusted Access

                            </h3>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>

<!-- WHAT WE PROTECT -->

<section class="py-20 bg-white">

    <div class="max-w-7xl mx-auto px-6">

        <div class="text-center">

            <span
                class="inline-flex items-center gap-2 px-5 py-2 rounded-full bg-[#F9A825]/10 text-[#F9A825] font-semibold">

                <ShieldCheck class="w-5 h-5" />

                Data Protection

            </span>

            <h2
                class="mt-6 text-4xl font-bold text-[#1F2937]">

                What We Protect

            </h2>

            <p
                class="mt-5 max-w-3xl mx-auto text-lg text-[#374151] leading-8">

                Every interaction on WorkSpace is secured.
                From your account information to booking history,
                we apply strict confidentiality practices to protect
                your data throughout its lifecycle.

            </p>

        </div>

        <div
            class="grid lg:grid-cols-2 gap-8 mt-16">

            <!-- Personal -->

            <div
                class="group bg-[#F7F8FA] rounded-3xl p-8 border border-[#E5E7EB] hover:border-[#F9A825] transition-all duration-300 hover:shadow-xl">

                <div
                    class="w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                    <Users
                        class="w-8 h-8 text-[#F9A825]" />

                </div>

                <h3
                    class="mt-7 text-2xl font-bold text-[#1F2937]">

                    Personal Information

                </h3>

                <p
                    class="mt-4 text-[#374151] leading-8">

                    Your name, email address, phone number,
                    and account details are stored securely and
                    only used to provide our services.

                </p>

            </div>

            <!-- Booking -->

            <div
                class="group bg-[#F7F8FA] rounded-3xl p-8 border border-[#E5E7EB] hover:border-[#F9A825] transition-all duration-300 hover:shadow-xl">

                <div
                    class="w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                    <Building2
                        class="w-8 h-8 text-[#F9A825]" />

                </div>

                <h3
                    class="mt-7 text-2xl font-bold text-[#1F2937]">

                    Booking Information

                </h3>

                <p
                    class="mt-4 text-[#374151] leading-8">

                    Reservation dates,
                    workspace selections,
                    invoices,
                    and booking history remain protected
                    throughout every transaction.

                </p>

            </div>

            <!-- Payment -->

            <div
                class="group bg-[#F7F8FA] rounded-3xl p-8 border border-[#E5E7EB] hover:border-[#F9A825] transition-all duration-300 hover:shadow-xl">

                <div
                    class="w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                    <CreditCard
                        class="w-8 h-8 text-[#F9A825]" />

                </div>

                <h3
                    class="mt-7 text-2xl font-bold text-[#1F2937]">

                    Payment Records

                </h3>

                <p
                    class="mt-4 text-[#374151] leading-8">

                    Payment confirmations and billing records
                    are processed using secure payment practices.
                    Sensitive financial information is never exposed.

                </p>

            </div>

            <!-- Database -->

            <div
                class="group bg-[#F7F8FA] rounded-3xl p-8 border border-[#E5E7EB] hover:border-[#F9A825] transition-all duration-300 hover:shadow-xl">

                <div
                    class="w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                    <Database
                        class="w-8 h-8 text-[#F9A825]" />

                </div>

                <h3
                    class="mt-7 text-2xl font-bold text-[#1F2937]">

                    Platform Activity

                </h3>

                <p
                    class="mt-4 text-[#374151] leading-8">

                    Favorites,
                    reviews,
                    notifications,
                    and account activity are securely stored
                    to improve your experience.

                </p>

            </div>

        </div>

    </div>

</section>

<!-- WHO CAN ACCESS -->

<section class="py-20 bg-[#F7F8FA]">

    <div class="max-w-7xl mx-auto px-6">

        <div class="text-center">

            <span
                class="inline-flex items-center gap-2 px-5 py-2 rounded-full bg-[#F9A825]/10 text-[#F9A825] font-semibold">

                <Lock class="w-5 h-5" />

                Access Control

            </span>

            <h2
                class="mt-6 text-4xl font-bold text-[#1F2937]">

                Who Can Access Your Information?

            </h2>

            <p
                class="mt-5 max-w-3xl mx-auto text-lg text-[#374151] leading-8">

                Access to customer information is strictly limited.
                Every role has clearly defined permissions to ensure
                confidentiality and responsible data handling.

            </p>

        </div>

        <div
            class="grid lg:grid-cols-3 gap-8 mt-16">

            <!-- Workspace Team -->

            <div
                class="bg-white rounded-[30px] overflow-hidden border border-[#E5E7EB] shadow-sm hover:shadow-xl transition">

                <div class="h-2 bg-[#F9A825]"></div>

                <div class="p-8">

                    <div
                        class="w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                        <ShieldCheck
                            class="w-8 h-8 text-[#F9A825]" />

                    </div>

                    <h3
                        class="mt-7 text-2xl font-bold text-[#1F2937]">

                        WorkSpace Team

                    </h3>

                    <p
                        class="mt-4 text-[#374151] leading-8">

                        Authorized administrators manage platform
                        operations, customer support, and account
                        verification while following strict internal
                        confidentiality procedures.

                    </p>

                    <ul
                        class="mt-8 space-y-4">

                        <li class="flex items-center gap-3">

                            <CheckCircle2
                                class="w-5 h-5 text-green-600" />

                            <span>Customer Support</span>

                        </li>

                        <li class="flex items-center gap-3">

                            <CheckCircle2
                                class="w-5 h-5 text-green-600" />

                            <span>Security Monitoring</span>

                        </li>

                        <li class="flex items-center gap-3">

                            <CheckCircle2
                                class="w-5 h-5 text-green-600" />

                            <span>Account Verification</span>

                        </li>

                    </ul>

                </div>

            </div>

            <!-- Office Owners -->

            <div
                class="bg-white rounded-[30px] overflow-hidden border border-[#E5E7EB] shadow-sm hover:shadow-xl transition">

                <div class="h-2 bg-[#F9A825]"></div>

                <div class="p-8">

                    <div
                        class="w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                        <Building2
                            class="w-8 h-8 text-[#F9A825]" />

                    </div>

                    <h3
                        class="mt-7 text-2xl font-bold text-[#1F2937]">

                        Office Owners

                    </h3>

                    <p
                        class="mt-4 text-[#374151] leading-8">

                        Property owners only access reservation
                        information related to offices they manage.
                        They cannot access unrelated customer data.

                    </p>

                    <ul
                        class="mt-8 space-y-4">

                        <li class="flex items-center gap-3">

                            <CheckCircle2
                                class="w-5 h-5 text-green-600" />

                            <span>Bookings</span>

                        </li>

                        <li class="flex items-center gap-3">

                            <CheckCircle2
                                class="w-5 h-5 text-green-600" />

                            <span>Office Availability</span>

                        </li>

                        <li class="flex items-center gap-3">

                            <XCircle
                                class="w-5 h-5 text-red-500" />

                            <span>No Payment Details</span>

                        </li>

                    </ul>

                </div>

            </div>

            <!-- Payment Providers -->

            <div
                class="bg-white rounded-[30px] overflow-hidden border border-[#E5E7EB] shadow-sm hover:shadow-xl transition">

                <div class="h-2 bg-[#F9A825]"></div>

                <div class="p-8">

                    <div
                        class="w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                        <CreditCard
                            class="w-8 h-8 text-[#F9A825]" />

                    </div>

                    <h3
                        class="mt-7 text-2xl font-bold text-[#1F2937]">

                        Payment Services

                    </h3>

                    <p
                        class="mt-4 text-[#374151] leading-8">

                        External payment providers receive only the
                        minimum information required to process
                        secure financial transactions.

                    </p>

                    <ul
                        class="mt-8 space-y-4">

                        <li class="flex items-center gap-3">

                            <CheckCircle2
                                class="w-5 h-5 text-green-600" />

                            <span>Transaction Verification</span>

                        </li>

                        <li class="flex items-center gap-3">

                            <CheckCircle2
                                class="w-5 h-5 text-green-600" />

                            <span>Secure Payment Processing</span>

                        </li>

                        <li class="flex items-center gap-3">

                            <XCircle
                                class="w-5 h-5 text-red-500" />

                            <span>No Account Passwords</span>

                        </li>

                    </ul>

                </div>

            </div>

        </div>

    </div>

</section>

<!-- SECURITY STANDARDS -->

<section class="py-20 bg-white">

    <div class="max-w-7xl mx-auto px-6">

        <div class="text-center">

            <span
                class="inline-flex items-center gap-2 px-5 py-2 rounded-full bg-[#F9A825]/10 text-[#F9A825] font-semibold">

                <ShieldCheck class="w-5 h-5"/>

                Security Standards

            </span>

            <h2
                class="mt-6 text-4xl font-bold text-[#1F2937]">

                Security Built Into Every Layer

            </h2>

            <p
                class="mt-5 max-w-3xl mx-auto text-lg text-[#374151] leading-8">

                We continuously improve our infrastructure,
                monitor our systems and follow best practices
                to keep your information protected.

            </p>

        </div>

        <div
            class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mt-16">

            <!-- Encryption -->

            <div
                class="bg-[#F7F8FA] rounded-3xl p-8 border border-[#E5E7EB] text-center hover:shadow-lg transition">

                <div
                    class="mx-auto w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                    <Lock class="w-8 h-8 text-[#F9A825]"/>

                </div>

                <h3
                    class="mt-6 text-3xl font-bold text-[#1F2937]">

                    256-bit

                </h3>

                <p
                    class="mt-3 text-[#374151]">

                    Encryption

                </p>

            </div>

            <!-- Monitoring -->

            <div
                class="bg-[#F7F8FA] rounded-3xl p-8 border border-[#E5E7EB] text-center hover:shadow-lg transition">

                <div
                    class="mx-auto w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                    <Activity class="w-8 h-8 text-[#F9A825]"/>

                </div>

                <h3
                    class="mt-6 text-3xl font-bold text-[#1F2937]">

                    24 / 7

                </h3>

                <p
                    class="mt-3 text-[#374151]">

                    Monitoring

                </p>

            </div>

            <!-- Access -->

            <div
                class="bg-[#F7F8FA] rounded-3xl p-8 border border-[#E5E7EB] text-center hover:shadow-lg transition">

                <div
                    class="mx-auto w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                    <Users class="w-8 h-8 text-[#F9A825]"/>

                </div>

                <h3
                    class="mt-6 text-3xl font-bold text-[#1F2937]">

                    Role-Based

                </h3>

                <p
                    class="mt-3 text-[#374151]">

                    Access Control

                </p>

            </div>

            <!-- Review -->

            <div
                class="bg-[#F7F8FA] rounded-3xl p-8 border border-[#E5E7EB] text-center hover:shadow-lg transition">

                <div
                    class="mx-auto w-16 h-16 rounded-2xl bg-[#F9A825]/10 flex items-center justify-center">

                    <BadgeCheck class="w-8 h-8 text-[#F9A825]"/>

                </div>

                <h3
                    class="mt-6 text-3xl font-bold text-[#1F2937]">

                    Regular

                </h3>

                <p
                    class="mt-3 text-[#374151]">

                    Security Reviews

                </p>

            </div>

        </div>

    </div>

</section>

<!-- CTA -->

<section class="pb-24 bg-[#F7F8FA]">

    <div class="max-w-7xl mx-auto px-6">

        <div
            class="rounded-[40px] overflow-hidden bg-[#1F2937]">

            <div
                class="grid lg:grid-cols-2">

                <!-- Left -->

                <div class="p-14">

                    <span
                        class="inline-flex items-center gap-2 text-[#F9A825] font-semibold">

                        <MessageCircleMore
                            class="w-5 h-5"/>

                        Need Help?

                    </span>

                    <h2
                        class="mt-6 text-4xl font-bold text-white leading-tight">

                        Questions About
                        Confidentiality?

                    </h2>

                    <p
                        class="mt-6 text-gray-300 leading-8 max-w-lg">

                        If you have questions about how we collect,
                        use or protect your information,
                        our support team will be happy to help.

                    </p>

                    <div
                        class="flex flex-wrap gap-5 mt-10">

                        <RouterLink
                            to="/contact"
                            class="bg-[#F9A825] hover:bg-yellow-500 transition text-white px-7 py-4 rounded-xl font-semibold">

                            Contact Support

                        </RouterLink>

                        <RouterLink
                            to="/privacy-policy"
                            class="border border-white/20 hover:bg-white/10 transition text-white px-7 py-4 rounded-xl">

                            Privacy Policy

                        </RouterLink>

                    </div>

                </div>

                <!-- Right -->

                <div
                    class="bg-[#111827] flex items-center justify-center p-14">

                    <div
                        class="space-y-6 w-full">

                        <div
                            class="flex items-center justify-between">

                            <span class="text-gray-300">

                                Platform Security

                            </span>

                            <span class="text-green-400">

                                Operational

                            </span>

                        </div>

                        <div
                            class="h-2 rounded-full bg-white/10 overflow-hidden">

                            <div
                                class="w-full h-full bg-green-500">

                            </div>

                        </div>

                        <div
                            class="grid grid-cols-2 gap-6 mt-10">

                            <div>

                                <p class="text-gray-400 text-sm">

                                    Encryption

                                </p>

                                <h3 class="text-white font-bold">

                                    Enabled

                                </h3>

                            </div>

                            <div>

                                <p class="text-gray-400 text-sm">

                                    Access Logs

                                </p>

                                <h3 class="text-white font-bold">

                                    Active

                                </h3>

                            </div>

                            <div>

                                <p class="text-gray-400 text-sm">

                                    Monitoring

                                </p>

                                <h3 class="text-white font-bold">

                                    Running

                                </h3>

                            </div>

                            <div>

                                <p class="text-gray-400 text-sm">

                                    Backups

                                </p>

                                <h3 class="text-white font-bold">

                                    Automated

                                </h3>

                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>
</div>
</template>
